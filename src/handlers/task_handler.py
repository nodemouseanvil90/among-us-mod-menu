"""Auto-task completion handler."""
from __future__ import annotations

from src.handlers.base import BaseHandler
from src.utils.offsets import resolve_offset


class TaskHandler(BaseHandler):
    name = "task"

    def process(self, ctx: dict) -> dict:
        if not self.enabled or not self.cfg.auto_tasks:
            return ctx
        addr = resolve_offset(ctx["handle"], self.cfg.offsets.task_counter)
        ctx.setdefault("patches", []).append(
            {"addr": addr, "value": 0, "source": self.name}
        )
        return ctx