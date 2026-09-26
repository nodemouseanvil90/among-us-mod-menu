"""Crewmate vision range handler."""
from __future__ import annotations

from src.handlers.base import BaseHandler


class VisionHandler(BaseHandler):
    name = "vision"

    def process(self, ctx: dict) -> dict:
        if not self.enabled:
            return ctx
        ctx["vision_range"] = self.cfg.vision_range
        return ctx