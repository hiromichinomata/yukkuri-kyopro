"""本文・README の相対リンクとアンカー（#見出し）が切れていないか。"""

import os
import re

import pytest
from conftest import ROOT

FILES = sorted(
    [p for p in (ROOT / "docs").glob("*.md")]
    + [p for p in (ROOT / "solutions").glob("*/*/README.md")]
    + [ROOT / "README.md", ROOT / "solutions" / "README.md"]
)


def slug(heading: str) -> str:
    """GitHub と同じ規則で見出しをアンカーにする（記号を消し、空白を - に）"""
    h = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return h.replace(" ", "-")


def anchors(path) -> set:
    text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
    return {slug(h) for h in re.findall(r"^#+ (.*)$", text, re.M)}


@pytest.mark.parametrize("path", FILES, ids=lambda p: str(p.relative_to(ROOT)))
def test_relative_links(path):
    text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
    broken = []
    for url in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"^[a-z]+://", url):
            continue
        target, _, frag = url.partition("#")
        dest = (path.parent / target).resolve() if target else path
        if not dest.exists():
            broken.append(url)
        elif frag and dest.suffix == ".md" and frag not in anchors(dest):
            broken.append(url)
    assert broken == []
