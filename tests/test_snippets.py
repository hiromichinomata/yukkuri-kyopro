"""本文のすべてのコードブロックと解答が、構文として正しいか。

- Python: AtCoder の PyPy（3.11）でも読める文法か（ast.parse の feature_version）
- Go: gofmt -e で構文エラーがないか（断片は関数で包んでから調べる）
解答へのリンクがない節のコード片も対象になる（中身の正しさは test_docs_code / test_docs_go が見る）。
"""

import ast

import pytest

import snippet_check as C

PY_BLOCKS = list(C.blocks("python"))
GO_BLOCKS = list(C.blocks("go"))
PY_FILES = sorted((C.ROOT / "solutions" / "python").glob("**/*.py")) + sorted((C.ROOT / "tests").glob("*.py"))


@pytest.mark.parametrize("doc,line,src", PY_BLOCKS, ids=[f"{d}:{l}" for d, l, _ in PY_BLOCKS])
def test_python_block_syntax(doc, line, src):
    assert C.python_error(src) is None


@pytest.mark.parametrize("doc,line,src", GO_BLOCKS, ids=[f"{d}:{l}" for d, l, _ in GO_BLOCKS])
def test_go_block_syntax(doc, line, src):
    assert C.go_error(src) is None


@pytest.mark.parametrize("path", PY_FILES, ids=lambda p: str(p.relative_to(C.ROOT)))
def test_python_file_is_py311(path):
    ast.parse(path.read_text(encoding="utf-8"), feature_version=C.PY_VERSION)


def test_checker_detects_errors():
    assert C.python_error("def f(:\n    pass\n") is not None
    assert C.python_error("match x:\n    case 1:\n        pass\n") is None  # 3.10+ の文法は OK
    assert C.go_error("x := []int{1, 2\n") is not None
    assert C.go_error("x := []int{1, 2}\nfmt.Println(x)\n") is None
