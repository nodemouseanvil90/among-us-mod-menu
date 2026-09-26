"""Role reveal / impostor hint handler."""
from __future__ import annotations

from src.handlers.base import BaseHandler


class RoleHandler(BaseHandler):
    name = "role"

    def process(self, ctx: dict) -> dict:
        if not self.enabled:
            return ctx
        ctx["role_hint"] = "reveal" if self.cfg.role_reveal else "hidden"
        return ctx