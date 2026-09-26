"""Base class for all mod handlers."""
from __future__ import annotations

from abc import ABC, abstractmethod


class BaseHandler(ABC):
    name: str = "base"

    def __init__(self, cfg) -> None:
        self.cfg = cfg
        self.enabled = True

    @abstractmethod
    def process(self, ctx: dict) -> dict:
        """Mutate and return the pipeline context."""

    def toggle(self, enabled: bool) -> None:
        self.enabled = enabled