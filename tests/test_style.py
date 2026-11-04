"""本文・README の表記の揺れ（用語・全角半角）がないか。

コードブロック・インラインコード・リンク先・URL は対象外。
直すときは、右側の「そろえる表記」に合わせる。
"""

import re

import pytest

from conftest import ROOT

FILES = (
    sorted((ROOT / "docs").glob("*.md"))
    + [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "solutions" / "README.md"]
    + sorted((ROOT / "solutions").glob("*/*/README.md"))
)

JA = r"[ぁ-んァ-ヶ一-龠]"
RULES = [
    # (見つけたら NG の表記, そろえる表記)
    (r"セグメントツリー|セグメント・ツリー", "セグメント木（略すときはセグ木）"),
    (r"テンプレ(?!ート)", "テンプレート"),
    (r"[01] ?始まり", "0-indexed / 1-indexed"),
    (r"Union ?Find|union-find|ユニオンファインド", "Union-Find（DSU）"),
    (r"Atcoder|ATCODER", "AtCoder"),
    (r"[Gg]olang|Go ?言語", "Go"),
    (r"(?<![\w/.-])python(?![\w/.-])", "Python"),
    (r"[Ａ-Ｚａ-ｚ０-９]", "半角英数字"),
    (r"　", "半角スペース"),
    (r"[，．]", "、。"),
    (r"～", "〜（波ダッシュ）"),
    (rf"{JA}[A-Za-z0-9]|[A-Za-z0-9]{JA}", "日本語と英数字の間に半角スペース"),
]


def prose_lines(path):
    inblock = False
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith("```"):
            inblock = not inblock
            continue
        if inblock:
            continue
        line = re.sub(r"`[^`]*`", " ", line)
        line = re.sub(r"\]\([^)]*\)", "] ", line)
        line = re.sub(r"https?://\S+", " ", line)
        line = re.sub(r"<[^>]+>", " ", line)
        yield i, line


@pytest.mark.parametrize("path", FILES, ids=lambda p: p.relative_to(ROOT).as_posix())
def test_style(path):
    bad = []
    for i, line in prose_lines(path):
        for pat, want in RULES:
            for m in re.finditer(pat, line):
                bad.append(f"{i}: 「{m.group()}」→ {want}")
    assert not bad, "\n".join(bad)
