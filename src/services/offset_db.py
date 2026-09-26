"""Loads offset tables from the bundled manifest."""
from __future__ import annotations

import json
from pathlib import Path


class OffsetDatabase:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._data: dict = {}

    def load(self) -> dict:
        self._data = json.loads(self.path.read_text(encoding="utf-8"))
        return self._data

    def get(self, key: str) -> int:
        return int(self._data.get(key, 0))