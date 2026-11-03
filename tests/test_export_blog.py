"""scripts/export_blog.py: 本文の相対リンクがすべて絶対 URL に置き換わるか。"""

import importlib.util
import re

from conftest import ROOT

spec = importlib.util.spec_from_file_location("export_blog", ROOT / "scripts" / "export_blog.py")
eb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eb)

REPO = "https://github.com/owner/repo"


def test_rules():
    t = eb.convert_text(
        "[a](../solutions/python/03/dsu/) [b](03.md#36-union-finddsu) [c](#local) [d](../LICENSE) "
        "[e](https://atcoder.jp/) `[f](03.md)`\n```\n[g](03.md)\n```",
        REPO, "main", None,
    )
    assert f"[a]({REPO}/tree/main/solutions/python/03/dsu)" in t
    assert f"[b]({REPO}/blob/main/docs/03.md#36-union-finddsu)" in t
    assert "[c](#local)" in t
    assert f"[d]({REPO}/blob/main/LICENSE)" in t
    assert "[e](https://atcoder.jp/)" in t
    assert "`[f](03.md)`" in t  # インラインコードはそのまま
    assert "[g](03.md)" in t  # コードブロックもそのまま


def test_chapter_url_template():
    t = eb.convert_text("[b](03.md#x)", REPO, "main", "https://blog.example/kyopro/{stem}/")
    assert t == "[b](https://blog.example/kyopro/03/#x)"


def test_all_docs_have_no_relative_links():
    for src in sorted((ROOT / "docs").glob("*.md")):
        out = eb.convert_text(src.read_text(encoding="utf-8"), REPO, "main", None)
        out = re.sub(r"```.*?```", "", out, flags=re.S)
        out = re.sub(r"`[^`\n]*`", "", out)
        rel = [u for u in re.findall(r"\]\(([^)\s]+)\)", out) if not re.match(r"^(https?://|#)", u)]
        assert rel == [], (src.name, rel[:5])
