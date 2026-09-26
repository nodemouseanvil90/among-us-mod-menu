"""Translates role hints into overlay-friendly state."""
from __future__ import annotations


class RoleProcessor:
    name = "role_processor"

    def __init__(self, cfg) -> None:
        self.cfg = cfg

    def process(self, ctx: dict) -> dict:
        hint = ctx.get("role_hint")
        if hint:
            ctx["overlay_role"] = hint.upper()
        return ctx