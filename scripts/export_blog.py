"""docs/*.md をブログ投稿用に書き出す。

本文の相対リンク（../solutions/...、03.md#...、../LICENSE）は、ブログ上ではそのままだと切れる。
これを絶対 URL に置き換えたコピーを出力ディレクトリに書き出す（docs/ 自体は変更しない）。

使い方:
    python3 scripts/export_blog.py                      # dist/blog/ に出力。章リンクは GitHub 上の md へ
    python3 scripts/export_blog.py --chapter-url 'https://example.com/kyopro/{stem}/'
        # 章リンクをブログの URL にする。{stem} は "03" や "00-toc"（拡張子なし）
    python3 scripts/export_blog.py --single dist/blog/yukkuri-kyopro.md
        # 目次（00-toc.md）を除く全章を 1 つの md にまとめる

--single のとき:
    章の前後のナビ（← 前 | 目次 | 次 →）と目次へのリンクを消す
    NN.md / NN.md#anchor / #anchor → まとめた md の中の見出しへのアンカー（GitHub と同じ規則で、重複には -1, -2 …）
    リンクの文字が "NN.md" のときは章の見出し（例: Part 1 — 灰色（Gray））に置き換える

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


LINK_FULL = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
TOC = "00-toc.md"


def slug(heading: str) -> str:
    """GitHub と同じ規則で見出しをアンカーにする（記号を消し、空白を - に）"""
    h = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return h.replace(" ", "-")


def outside_fences(lines):
    """(行番号, 行, コードブロックの外か) を返す"""
    in_fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            yield i, line, False
        else:
            yield i, line, not in_fence


def build_single(repo: str, branch: str) -> str:
    chapters = [p for p in sorted(DOCS.glob("*.md")) if p.name != TOC]
    texts = {}
    titles = {}
    anchor_map = {}  # (章のファイル名, 章の中でのアンカー) -> まとめた md でのアンカー
    used = {}
    for src in chapters:
        lines = []
        for _, line, outside in outside_fences(src.read_text(encoding="utf-8").split("\n")):
            if outside and (line.startswith("← ") or (line.startswith("|") and f"({TOC})" in line)):
                continue  # 章のナビと、目次へのリンクだけの表の行
            lines.append(line)
        # 消したナビの前後に残る区切り線と空行を詰める
        text = "\n".join(lines)
        text = re.sub(r"(\n---\n)(\s*---\n)+", r"\1", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        text = re.sub(r"\n+---$", "", text).strip()
        texts[src.name] = text
        local = {}
        for _, line, outside in outside_fences(text.split("\n")):
            m = re.match(r"^(#+) (.*)$", line) if outside else None
            if not m:
                continue
            s = slug(m.group(2))
            n = local.get(s, 0)
            local[s] = n + 1
            g = used.get(s, 0)
            used[s] = g + 1
            anchor_map[(src.name, s if n == 0 else f"{s}-{n}")] = s if g == 0 else f"{s}-{g}"
            if src.name not in titles:
                titles[src.name] = (m.group(2).strip(), anchor_map[(src.name, s)])

    def anchor(name: str, frag: str) -> str:
        if not frag:
            return "#" + titles[name][1]
        if (name, frag) not in anchor_map:
            raise ValueError(f"{name} に見出し #{frag} がない")
        return "#" + anchor_map[(name, frag)]

    out = []
    for src in chapters:
        lines = []
        for _, line, outside in outside_fences(texts[src.name].split("\n")):
            if not outside:
                lines.append(line)
                continue
            saved = []

            def stash(m):
                saved.append(m.group(0))
                return f"\0{len(saved) - 1}\0"

            def repl(m):
                label, target = m.group(1), m.group(2)
                path, _, frag = target.partition("#")
                if path == TOC:
                    return label  # 目次はないのでリンクを外す
                if path == "" and target.startswith("#"):
                    return f"[{label}]({anchor(src.name, frag)})"
                if re.fullmatch(r"\d\d\.md", path) and (DOCS / path).exists():
                    if label == path:
                        label = titles[path][0]
                    return f"[{label}]({anchor(path, frag)})"
                return f"[{label}]({convert_target(target, repo, branch, None)})"

            body = INLINE_CODE.sub(stash, line)
            body = LINK_FULL.sub(repl, body)
            body = re.sub(r"\0(\d+)\0", lambda m: saved[int(m.group(1))], body)
            lines.append(body)
        out.append("\n".join(lines))
    return "\n\n---\n\n".join(out) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(ROOT / "dist" / "blog"), help="出力先（既定: dist/blog）")
    ap.add_argument("--repo", default="https://github.com/hiromichinomata/yukkuri-kyopro")
    ap.add_argument("--branch", default="main")
    ap.add_argument("--chapter-url", default=None, help="章リンクの URL テンプレート。{stem} が章のファイル名（拡張子なし）")
    ap.add_argument("--single", default=None, help="目次を除く全章を 1 つの md にまとめてこのパスに書き出す")
    args = ap.parse_args(argv)
    if args.single:
        dest = Path(args.single)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(build_single(args.repo.rstrip("/"), args.branch), encoding="utf-8")
        print(f"docs/*.md -> {dest}")
        return 0
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
