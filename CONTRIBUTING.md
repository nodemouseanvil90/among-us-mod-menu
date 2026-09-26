# Contributing to among-us-mod-menu

Thanks for helping improve the Among Us ModMenu tooling. This project targets
Windows desktop usage and is written primarily in Python, with a small C++
helper for memory offset scanning.

## Ground rules

1. Only test against your own local lobbies / offline sessions.
2. Never commit game memory dumps or offset tables extracted at runtime.
3. Keep PRs scoped: one handler, processor, or driver per change.

## Local setup

```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.bootstrap.launch
```

## Style

- Black formatting, 100 col limit.
- Type hints on all public functions.
- Log via `src.utils.logger`, never `print()`.

## Adding a new mod handler

1. Drop a module in `src/handlers/` implementing `BaseHandler`.
2. Register it in `src/handlers/registry.py`.
3. Add a test under `tests/`.