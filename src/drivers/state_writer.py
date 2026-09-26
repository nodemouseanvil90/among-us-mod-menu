"""Writes resolved patches into the target process."""
from __future__ import annotations

from src.utils.logger import get_logger

log = get_logger("state_writer")


class StateWriter:
    name = "state_writer"

    def __init__(self, cfg) -> None:
        self.cfg = cfg
        self.dry_run = cfg.dry_run

    def process(self, ctx: dict) -> dict:
        handle = ctx.get("handle")
        for patch in ctx.get("patches", []):
            if self.dry_run:
                log.debug("dry-run patch %s", patch)
                continue
            handle.write(patch["addr"], patch["value"])
        ctx["patches"] = []
        return ctx