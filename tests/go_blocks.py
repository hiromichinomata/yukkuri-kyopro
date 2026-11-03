"""本文の Go コードブロックと solutions/go の main.go を、トップレベルの宣言単位で突き合わせる補助。"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"


def strip_comments(src: str) -> str:
    out = []
    for line in src.split("\n"):
        # 文字列リテラル内の // は少ないので、簡易的に行コメントを落とす
        m = re.search(r'//(?=(?:[^"`]*["`][^"`]*["`])*[^"`]*$)', line)
        out.append(line[: m.start()] if m else line)
    src = "\n".join(out)
    return re.sub(r"/\*.*?\*/", "", src, flags=re.S)


def norm(src: str) -> str:
    """コメント・空白の違いを無視した比較用の文字列"""
    return re.sub(r"\s+", "", strip_comments(src))


def top_decls(src: str) -> dict:
    """トップレベルの func / type 宣言を {名前: 本文} で返す（中括弧の対応で範囲を取る）"""
    decls = {}
    lines = src.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^(func(?: \([^)]*\))? (\w+)|type (\w+))", lines[i])
        if not m:
            i += 1
            continue
        name = m.group(2) or m.group(3)
        if m.group(0).startswith("func ("):
            recv = re.match(r"^func \(\w*\s*\*?(\w+)\)", lines[i])
            name = f"{recv.group(1)}.{name}" if recv else name
        depth, j, buf = 0, i, []
        while j < len(lines):
            buf.append(lines[j])
            code = strip_comments(lines[j])
            depth += code.count("{") - code.count("}")
            if depth <= 0 and ("{" in "".join(buf) or not lines[i].rstrip().endswith("{")):
                break
            j += 1
        decls[name] = "\n".join(buf)
        i = j + 1
    return decls


def doc_go_blocks():
    """(docファイル, 節の先頭行, ブロック, 対応する solutions/go のディレクトリ) を列挙"""
    for doc in sorted(DOCS.glob("*.md")):
        text = doc.read_text(encoding="utf-8")
        pattern = r"\n(?=## )" if doc.name == "11.md" else r"\n(?=#{2,4} )"
        for sec in re.split(pattern, text):
            dirs = sorted(set(re.findall(r"solutions/(?:python|go)/(\d\d/[\w]+)/", sec)))
            for blk in re.findall(r"```go\n(.*?)```", sec, re.S):
                yield doc.name, sec.split("\n", 1)[0][:40], blk, dirs
