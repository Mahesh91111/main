import os
import sys
from pathlib import Path

backend_root = Path(__file__).resolve().parent
if str(backend_root) not in sys.path:
    sys.path.insert(0, str(backend_root))

if len(sys.argv) < 2:
    raise SystemExit("Usage: python run_module.py <module_path>")

module_name = sys.argv[1]
if module_name.startswith("."):
    module_name = module_name[1:]

__import__(module_name)
