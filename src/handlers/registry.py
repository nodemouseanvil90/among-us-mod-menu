"""Builds the handler chain from configuration."""
from __future__ import annotations

from src.handlers.base import BaseHandler
from src.handlers.role_handler import RoleHandler
from src.handlers.speed_handler import SpeedHandler
from src.handlers.task_handler import TaskHandler
from src.handlers.vision_handler import VisionHandler

HANDLER_MAP = {
    "role": RoleHandler,
    "speed": SpeedHandler,
    "task": TaskHandler,
    "vision": VisionHandler,
}


def build_handlers(cfg) -> list[BaseHandler]:
    handlers: list[BaseHandler] = []
    for key in cfg.enabled_handlers:
        cls = HANDLER_MAP.get(key)
        if cls is None:
            continue
        handlers.append(cls(cfg))
    return handlers