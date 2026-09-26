"""Offset resolution helpers."""
from __future__ import annotations


def resolve_offset(handle, base_offset: int) -> int:
    if not base_offset:
        return 0
    return handle.base_address + base_offset


def hexfmt(addr: int) -> str:
    return f"0x{addr:X}"