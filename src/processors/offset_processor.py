"""Resolves and validates memory offsets before patching."""
from __future__ import annotations

from src.utils.logger import get_logger

log = get_logger("offset_processor")


class OffsetProcessor:
    name = "offset_processor"

    def __init__(self, cfg) -> None:
        self.cfg = cfg

    def process(self, ctx: dict) -> dict:
        patches = ctx.get("patches", [])
        valid = [p for p in patches if p.get("addr")]
        if len(valid) != len(patches):
            log.warning("Dropped %d invalid offsets", len(patches) - len(valid))
        ctx["patches"] = valid
        return ctx