"""Job descriptor used to schedule mod toggles."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class JobKind(str, Enum):
    TOGGLE = "toggle"
    PATCH = "patch"
    SCAN = "scan"


@dataclass
class ModJob:
    kind: JobKind
    handler: str
    payload: dict = field(default_factory=dict)
    priority: int = 5
    enabled: bool = True