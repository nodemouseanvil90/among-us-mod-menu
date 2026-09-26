"""Entry point for the Among Us ModMenu desktop tool."""
from __future__ import annotations

import sys

from src.bootstrap.app import ModMenuApp
from src.utils.logger import get_logger

log = get_logger("bootstrap")


def main() -> int:
    log.info("Starting among-us-mod-menu (2026 build)")
    app = ModMenuApp.from_config("config/default.toml")
    try:
        app.run()
    except KeyboardInterrupt:
        log.warning("Interrupted by user")
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())