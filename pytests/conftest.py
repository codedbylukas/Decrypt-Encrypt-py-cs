"""
conftest.py – executed before any test module is imported.

Mocks out the `cs.module` dependency (which requires pythonnet / .NET runtime)
and the interactive prompts that run at module-level inside main.py, so that
`import main` works in a plain Python test environment.
"""

import sys
from types import ModuleType
from unittest.mock import MagicMock

# ── 1. Mock cs.module before main.py is ever imported ──────────────────────
cs_pkg = ModuleType("cs")
cs_module = ModuleType("cs.module")

cs_module.clear = MagicMock()
cs_module.encrypt_file = MagicMock()
cs_module.decrypt_file = MagicMock()

sys.modules["cs"] = cs_pkg
sys.modules["cs.module"] = cs_module

# ── 2. Mock the interactive prompt helpers so module-level calls in
#       main.py return deterministic values without blocking on stdin ────────
import py_src.choice as _choice  # noqa: E402

_choice.ask_for_password = MagicMock(return_value="test_password")
_choice.ask_for_salt = MagicMock(return_value="test_salt")
_choice.ask_for_multiprocessing = MagicMock(return_value=False)
