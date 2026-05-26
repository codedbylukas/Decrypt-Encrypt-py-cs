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

# ── 2. Temporarily mock the interactive prompt helpers ONLY while main.py
#       is imported, so its module-level calls don't block on stdin.
#       After the import the originals are restored, so test_choice.py
#       still sees real FunctionType objects. ─────────────────────────────────
from unittest.mock import patch  # noqa: E402

with patch("py_src.choice.ask_for_password", return_value="test_password"), \
     patch("py_src.choice.ask_for_salt", return_value="test_salt"), \
     patch("py_src.choice.ask_for_multiprocessing", return_value=False):
    import main  # noqa: E402, F401  — triggers the module-level calls under mocks
