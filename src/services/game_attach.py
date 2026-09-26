"""Locates and attaches to the Among Us process."""
from __future__ import annotations

import pymem

from src.utils.logger import get_logger

log = get_logger("attach")


class GameAttachService:
    def __init__(self, process_name: str) -> None:
        self.process_name = process_name

    def connect(self):
        log.info("Looking for process %s", self.process_name)
        return pymem.Pymem(self.process_name)