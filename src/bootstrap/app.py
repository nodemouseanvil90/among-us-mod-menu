"""Application wiring: builds the pipeline from config."""
from __future__ import annotations

from dataclasses import dataclass

from src.core.pipeline import Pipeline
from src.drivers.overlay_driver import OverlayDriver
from src.drivers.state_writer import StateWriter
from src.handlers.registry import build_handlers
from src.processors.offset_processor import OffsetProcessor
from src.processors.role_processor import RoleProcessor
from src.services.game_attach import GameAttachService
from src.utils.config import load_config
from src.utils.logger import get_logger

log = get_logger("app")


@dataclass
class ModMenuApp:
    pipeline: Pipeline
    attach: GameAttachService

    @classmethod
    def from_config(cls, path: str) -> "ModMenuApp":
        cfg = load_config(path)
        attach = GameAttachService(process_name=cfg.process_name)
        handlers = build_handlers(cfg)
        processors = [OffsetProcessor(cfg), RoleProcessor(cfg)]
        drivers = [StateWriter(cfg), OverlayDriver(cfg)]
        pipeline = Pipeline(handlers=handlers, processors=processors, drivers=drivers)
        return cls(pipeline=pipeline, attach=attach)

    def run(self) -> None:
        handle = self.attach.connect()
        log.info("Attached to Among Us process, pid=%s", handle.pid)
        self.pipeline.start(handle)