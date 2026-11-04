"""本文に載せた「プログラム全体」のコードブロックが、テスト済みの解答ファイルと同じか。

本文の節（見出しごと）が solutions/{python,go}/NN/<dir>/ へリンクしていて、その節に
`if __name__ == "__main__":` を含む Python ブロック、または `package main` で始まる Go ブロックがあれば、
リンク先の main.py / main.go と一致することを確かめる（コメント・空白・docstring の違いは無視する）。
"""

import ast
import re

import pytest

import go_blocks as G
from conftest import ROOT

LANGS = {"python": ("main.py", 'if __name__ == "__main__":'), "go": ("main.go", "package main")}


def norm(src: str, lang: str) -> str:
    if lang == "go":
        return G.norm(src)
    tree = ast.parse(src)
    for node in ast.walk(tree):  # docstring は説明文なので比べない
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef)) and node.body:
            first = node.body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
                node.body = node.body[1:] or [ast.Pass()]
    return ast.dump(tree)


def cases():
    out = []
    for doc in sorted((ROOT / "docs").glob("0[0-8].md")):
        for sec in re.split(r"\n(?=#{2,4} )", doc.read_text(encoding="utf-8")):
            head = sec.splitlines()[0]
            for lang, (fname, mark) in LANGS.items():
                dirs = sorted(set(re.findall(rf"solutions/{lang}/(\d\d/[\w-]+)/", sec)))
                blocks = [b for b in re.findall(rf"```{lang}\n(.*?)```", sec, re.S) if mark in b]
                if len(dirs) == 1 and blocks:
                    for b in blocks:
                        out.append((f"{doc.name} {head.strip('# ')} {lang}", b, dirs[0], lang, fname))
    return out


CASES = cases()


@pytest.mark.parametrize("case", CASES, ids=lambda c: c[0])
def test_doc_program_matches_solution(case):
    _, block, d, lang, fname = case
    path = ROOT / "solutions" / lang / d / fname
    assert path.exists(), path
    assert norm(block, lang) == norm(path.read_text(encoding="utf-8"), lang), f"solutions/{lang}/{d}/{fname} と食い違い"
