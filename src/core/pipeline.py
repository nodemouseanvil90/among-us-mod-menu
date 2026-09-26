"""Worker-style pipeline: handlers -> processors -> drivers."""
from __future__ import annotations

import threading
import time
from typing import Iterable, Protocol

from src.utils.logger import get_logger

log = get_logger("pipeline")


class Stage(Protocol):
    name: str

    def process(self, ctx: dict) -> dict: ...


class Pipeline:
    def __init__(self, handlers: Iterable[Stage], processors: Iterable[Stage],
                 drivers: Iterable[Stage]) -> None:
        self.handlers = list(handlers)
        self.processors = list(processors)
        self.drivers = list(drivers)
        self._stop = threading.Event()

    def start(self, handle) -> None:
        ctx: dict = {"handle": handle, "tick": 0}
        while not self._stop.is_set():
            ctx["tick"] += 1
            for stage in (*self.handlers, *self.processors, *self.drivers):
                try:
                    ctx = stage.process(ctx)
                except Exception as exc:  # keep the loop alive
                    log.error("Stage %s failed: %s", stage.name, exc)
            time.sleep(0.05)

    def stop(self) -> None:
        self._stop.set()