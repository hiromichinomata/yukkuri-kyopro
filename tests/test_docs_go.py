"""本文の Go コードブロックが、テスト済みの solutions/go/NN/<dir>/main.go と食い違っていないか。

本文の節から solutions/{python,go}/NN/<dir>/ へリンクしているとき、その節の Go ブロックにある
トップレベルの func / type のうち、main.go に同名のものがあれば、コメントと空白を除いて一致することを確かめる。
（Go の解答は main_test.go で愚直解と比べているので、本文がそれと同じなら本文も正しい）
"""

import pytest

import go_blocks as G

CASES = []
for doc, head, blk, dirs in G.doc_go_blocks():
    sols = {}
    for d in dirs:
        p = G.ROOT / "solutions" / "go" / d / "main.go"
        if p.exists():
            for name, body in G.top_decls(p.read_text(encoding="utf-8")).items():
                sols.setdefault(name, (d, body))
    for name, body in G.top_decls(blk).items():
        if name != "main" and name in sols:
            CASES.append((f"{doc} {head.strip('# ')} {name}", body, sols[name]))


def test_some_blocks_are_checked():
    assert len(CASES) >= 100


@pytest.mark.parametrize("case", CASES, ids=lambda c: c[0])
def test_doc_go_matches_solution(case):
    _, body, (d, sol) = case
    assert G.norm(body) == G.norm(sol), f"solutions/go/{d}/main.go と食い違い"
