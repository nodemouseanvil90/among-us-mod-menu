"""Renders the in-game overlay state (external window)."""
from __future__ import annotations


class OverlayDriver:
    name = "overlay_driver"

    def __init__(self, cfg) -> None:
        self.cfg = cfg
        self.lines: list[str] = []

    def process(self, ctx: dict) -> dict:
        self.lines = []
        if "overlay_role" in ctx:
            self.lines.append(f"role: {ctx['overlay_role']}")
        if "vision_range" in ctx:
            self.lines.append(f"vision: {ctx['vision_range']}")
        ctx["overlay"] = list(self.lines)
        return ctx