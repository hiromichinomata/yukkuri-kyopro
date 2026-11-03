"""solutions/python/NN/<name>/main.py を「モジュール」として読み込むためのヘルパー。"""

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = ROOT / "solutions" / "python"
GO = ROOT / "solutions" / "go"


def load(rel: str):
    """load("04/segtree") → solutions/python/04/segtree/main.py をモジュールとして返す"""
    path = PY / rel / "main.py"
    name = "sol_" + rel.replace("/", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod
