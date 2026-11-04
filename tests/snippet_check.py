"""本文のコードブロックが構文として正しいかを調べる補助（断片も扱えるように包んでからパースする）。"""

import ast
import re
import shutil
import subprocess
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PY_VERSION = (3, 11)  # AtCoder の PyPy は 3.11 なので、それ以下の文法に収める


def blocks(lang: str):
    """(ファイル名, 行番号, コード) を列挙"""
    for doc in sorted(DOCS.glob("*.md")):
        text = doc.read_text(encoding="utf-8")
        for m in re.finditer(rf"^```{lang}\n(.*?)^```", text, re.S | re.M):
            yield doc.name, text[: m.start()].count("\n") + 1, m.group(1)


def python_error(src: str):
    """パースできなければエラー文字列、できれば None"""
    src = textwrap.dedent(src)
    try:
        ast.parse(src, feature_version=PY_VERSION)
        return None
    except SyntaxError as e:
        # return / continue だけの断片は関数・ループで包んで再挑戦
        wrapped = "def _f():\n    for _ in []:\n" + textwrap.indent(src, " " * 8)
        try:
            ast.parse(wrapped, feature_version=PY_VERSION)
            return None
        except SyntaxError:
            return f"{e.msg} (line {e.lineno})"


def _gofmt_ok(code: str):
    r = subprocess.run(["gofmt", "-e"], input=code, capture_output=True, text=True)
    return r.returncode == 0, r.stderr.strip().split("\n")[0]


def _split_decls(src: str):
    """トップレベルの import / func / type 宣言（列 0 の } や ) まで）と、それ以外の文に分ける"""
    decls, stmts, lines, i = [], [], src.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        if re.match(r"^(func|type|import)\b", ln):
            j = i
            if ln.rstrip().endswith("{") or ln.rstrip().endswith("("):
                while j < len(lines) and lines[j] not in ("}", ")"):
                    j += 1
            decls += lines[i : j + 1]
            i = j + 1
        else:
            stmts.append(ln)
            i += 1
    return "\n".join(decls), "\n".join(stmts)


def go_error(src: str):
    """断片を 3 通りに包んで gofmt -e にかける。どれかで通れば OK"""
    if shutil.which("gofmt") is None:
        return None
    if re.search(r"^package \w+", src, re.M):
        return None if _gofmt_ok(src)[0] else _gofmt_ok(src)[1]
    decls, stmts = _split_decls(src)
    candidates = [
        "package main\n" + src,
        "package main\nfunc _() {\n" + src + "\n}\n",
        "package main\n" + decls + "\nfunc _() {\n" + stmts + "\n}\n",
    ]
    errs = []
    for code in candidates:
        ok, err = _gofmt_ok(code)
        if ok:
            return None
        errs.append(err)
    return errs[-1]
