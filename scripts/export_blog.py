"""docs/*.md をブログ投稿用に書き出す。

本文の相対リンク（../solutions/...、03.md#...、../LICENSE）は、ブログ上ではそのままだと切れる。
これを絶対 URL に置き換えたコピーを出力ディレクトリに書き出す（docs/ 自体は変更しない）。

使い方:
    python3 scripts/export_blog.py                      # dist/blog/ に出力。章リンクは GitHub 上の md へ
    python3 scripts/export_blog.py --chapter-url 'https://example.com/kyopro/{stem}/'
        # 章リンクをブログの URL にする。{stem} は "03" や "00-toc"（拡張子なし）

置き換えの規則:
    ../solutions/...      → {repo}/tree/{branch}/solutions/...（ファイルなら blob）
    ../LICENSE などの他ファイル → {repo}/blob/{branch}/...
    NN.md / NN.md#anchor   → --chapter-url（なければ {repo}/blob/{branch}/docs/NN.md）+ #anchor
    #anchor（同じ章の中）   → そのまま
コードブロック（``` で囲まれた部分）とインラインコードの中は書き換えない。
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
LINK = re.compile(r"(\]\()([^)\s]+)(\))")
INLINE_CODE = re.compile(r"(`+)(.+?)\1")


def convert_target(target: str, repo: str, branch: str, chapter_url: str | None) -> str:
    if re.match(r"^[a-z]+://", target) or target.startswith(("#", "mailto:")):
        return target
    path, _, frag = target.partition("#")
    frag = f"#{frag}" if frag else ""
    resolved = (DOCS / path).resolve()
    try:
        rel = resolved.relative_to(ROOT).as_posix()
    except ValueError:
        raise ValueError(f"リポジトリ外を指すリンク: {target}")
    if not resolved.exists():
        raise ValueError(f"存在しないパスへのリンク: {target}")
    if rel.startswith("docs/") and rel.endswith(".md"):
        stem = Path(rel).stem
        if chapter_url:
            return chapter_url.format(stem=stem) + frag
        return f"{repo}/blob/{branch}/{rel}{frag}"
    kind = "tree" if resolved.is_dir() else "blob"
    return f"{repo}/{kind}/{branch}/{rel}{frag}"


def convert_text(text: str, repo: str, branch: str, chapter_url: str | None) -> str:
    out = []
    in_fence = False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        # インラインコードを一時的に退避してからリンクを置き換える
        saved = []

        def stash(m):
            saved.append(m.group(0))
            return f"\0{len(saved) - 1}\0"

        body = INLINE_CODE.sub(stash, line)
        body = LINK.sub(lambda m: m.group(1) + convert_target(m.group(2), repo, branch, chapter_url) + m.group(3), body)
        body = re.sub(r"\0(\d+)\0", lambda m: saved[int(m.group(1))], body)
        out.append(body)
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(ROOT / "dist" / "blog"), help="出力先（既定: dist/blog）")
    ap.add_argument("--repo", default="https://github.com/hiromichinomata/yukkuri-kyopro")
    ap.add_argument("--branch", default="main")
    ap.add_argument("--chapter-url", default=None, help="章リンクの URL テンプレート。{stem} が章のファイル名（拡張子なし）")
    args = ap.parse_args(argv)
    if args.chapter_url and "{stem}" not in args.chapter_url:
        ap.error("--chapter-url には {stem} を含めてください")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for src in sorted(DOCS.glob("*.md")):
        text = convert_text(src.read_text(encoding="utf-8"), args.repo.rstrip("/"), args.branch, args.chapter_url)
        (out / src.name).write_text(text, encoding="utf-8")
        print(f"{src.relative_to(ROOT)} -> {out / src.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
