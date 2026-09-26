from src.handlers.speed_handler import SpeedHandler
from src.utils.config import AppConfig


class _Handle:
    base_address = 0x1000


def test_speed_handler_emits_patch():
    cfg = AppConfig(offsets={"player_speed": 0x20}, speed_multiplier=3.0)
    handler = SpeedHandler(cfg)
    ctx = handler.process({"handle": _Handle()})
    assert ctx["patches"][0]["value"] == 3.0


def test_speed_handler_disabled():
    cfg = AppConfig(offsets={"player_speed": 0x20})
    handler = SpeedHandler(cfg)
    handler.toggle(False)
    ctx = handler.process({"handle": _Handle()})
    assert "patches" not in ctx