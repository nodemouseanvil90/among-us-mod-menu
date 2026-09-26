"""Player speed modifier handler."""
from __future__ import annotations

from src.handlers.base import BaseHandler
from src.utils.offsets import resolve_offset


class SpeedHandler(BaseHandler):
    name = "speed"

    def process(self, ctx: dict) -> dict:
        if not self.enabled:
            return ctx
        addr = resolve_offset(ctx["handle"], self.cfg.offsets.player_speed)
        ctx.setdefault("patches", []).append(
            {"addr": addr, "value": self.cfg.speed_multiplier, "source": self.name}
        )
        return ctx