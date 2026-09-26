"""TOML-backed configuration loader."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import tomli


@dataclass
class AppConfig:
    process_name: str = "Among Us.exe"
    dry_run: bool = False
    enabled_handlers: list[str] = field(default_factory=lambda: ["speed", "role"])
    speed_multiplier: float = 1.0
    role_reveal: bool = True
    auto_tasks: bool = False
    vision_range: float = 1.0
    offsets: dict = field(default_factory=dict)


def load_config(path: str) -> AppConfig:
    raw = tomli.loads(Path(path).read_text(encoding="utf-8"))
    return AppConfig(**raw)