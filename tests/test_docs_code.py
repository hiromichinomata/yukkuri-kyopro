"""本文（docs/NN.md）の Python コードブロックを、解答と同じテストにかける。

本文のブロックが定義する関数・クラスで、同じ Part の解答（solutions/python/NN/*/main.py）を
上書きしたモジュールを作り、test_templates.py の各テストを実行する。
"""

import ast
import re
import types
from pathlib import Path

import pytest

import conftest
import test_templates

DOCS = conftest.ROOT / "docs"


def doc_blocks(part: str, rel: str):
    """見出しで区切った節のうち、solutions/python/<rel>/ へのリンクがある節の Python ブロック"""
    text = (DOCS / f"{part}.md").read_text(encoding="utf-8")
    sections = re.split(r"\n(?=#{2,4} )", text)
    out = []
    for sec in sections:
        if f"solutions/python/{rel}/" in sec:
            out += re.findall(r"```python\n(.*?)```", sec, re.S)
    return out


def stub_names(src: str):
    """本体が `...`（とコメント・docstring）だけの関数名。「テンプレは solutions 参照」の骨組み"""
    def is_const(s, typ):
        return isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant) and isinstance(s.value.value, typ)

    out = set()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef):
            body = [s for s in node.body if not is_const(s, str)]  # docstring を除く
            if len(body) == 1 and is_const(body[0], type(...)):
                out.add(node.name)
    return out


def defined_names(src: str):
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return set()
    return {n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name != "main"}


def doc_override_loader(used):
    """load(rel) の代わり: 解答モジュールに、本文で同名定義されたものを上書きして返す"""
    orig = conftest.load

    def load(rel):
        mod = orig(rel)
        part = rel.split("/")[0]
        names = {k for k, v in vars(mod).items() if isinstance(v, (types.FunctionType, type)) and v.__module__ == mod.__name__}
        ns = types.ModuleType(mod.__name__ + "_doc")
        ns.__dict__.update(vars(mod))
        for blk in doc_blocks(part, rel):
            hit = defined_names(blk) & names
            if not hit:
                continue
            g = dict(ns.__dict__)
            try:
                exec(compile(blk, f"docs/{part}.md", "exec"), g)
            except Exception:
                continue  # 断片的なブロック（未定義の変数を使う例など）は対象外
            stubs = stub_names(blk)
            for k in hit:
                new, old = g[k], getattr(mod, k)
                if isinstance(new, type):
                    # 本文のクラスは一部のメソッドだけのことが多い → 本文にあるメソッドだけ差し替える
                    meths = {m: f for m, f in vars(new).items() if callable(f) and m not in stubs}
                    if not meths:
                        continue
                    new = type(k, (old,), meths)
                elif k in stubs:
                    continue
                setattr(ns, k, new)
                used.add(f"{part}:{k}")
        return ns

    return load


TESTS = [getattr(test_templates, n) for n in dir(test_templates) if n.startswith("test_")]


@pytest.mark.parametrize("fn", TESTS, ids=lambda f: f.__name__)
def test_doc_version(fn, monkeypatch):
    used = set()
    monkeypatch.setattr(test_templates, "load", doc_override_loader(used))
    fn()
    if not used:
        pytest.skip("本文に対応するコードブロックなし")
