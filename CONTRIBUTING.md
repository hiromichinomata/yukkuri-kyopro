# 保守メモ

教材の本文（`docs/`）と解答（`solutions/`）を直す人向けのメモです。学習には不要です。

## テスト

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

python3 -m pytest                  # Python（tests/ と solutions/python/）。Python と Go の出力比較も含む
python3 -m pytest -m "not parity"  # 出力比較（Go のビルドで 1 分ほどかかる）を除いて手早く
go test ./solutions/go/...         # Go（各ディレクトリの main_test.go）
```

| テスト | 確かめること |
|--------|--------------|
| `tests/test_templates.py`、`tests/test_problems.py` | テンプレートと解答を、小さいランダム入力で愚直解（全探索）と比べる |
| `tests/test_docs_code.py` | 本文に載っている Python のコードブロックそのものを、上と同じテストにかける |
| `tests/test_docs_go.py` | 本文の Go の関数・型が `solutions/go/` の `main.go` と一致する |
| `tests/test_docs_programs.py` | 本文に載せたプログラム全体（`main` まで含むブロック）が、リンク先の `main.py` / `main.go` と一致する |
| `tests/test_snippets.py` | 本文のすべてのコードブロックが文法上正しい（Python 3.11 / `gofmt`） |
| `tests/test_py_go_parity.py` | 同じディレクトリの Python 版と Go 版が、同じ入力に同じ出力を返す |
| `tests/test_links.py` | 本文・README の相対リンクと見出しへのアンカーが切れていない |

テンプレートを書き換えたら、テストが通ることを確認してから本文に反映してください。出力は AtCoder と同じく、列は空白区切り・真偽は `Yes` / `No` にそろえています。

AtCoder から取得したテストデータは **コミットしない**（`.gitignore` 済み）。入力例 1 だけを `input.txt` として置きます。

## ブログ用に書き出す

本文の解答リンクは `../solutions/...` のような相対パスなので、md をそのままブログに貼ると切れます。次のスクリプトで、相対リンクを GitHub の URL に置き換えたコピーを `dist/blog/` に書き出します（`docs/` は変更しません）。

```bash
python3 scripts/export_blog.py                                            # 章どうしのリンクも GitHub 上の md へ
python3 scripts/export_blog.py --chapter-url 'https://example.com/kyopro/{stem}/'  # 章どうしのリンクをブログの URL に
python3 scripts/export_blog.py --branch v2                                # main 以外のブランチを指す場合
```

章内の見出しへのリンク（`#36-union-finddsu` など）は GitHub と同じ規則のまま残します。

## 執筆（Cursor Agent）

章の執筆・`solutions/` 同期はプロジェクトスキル **yukkuri-kyopro-chapter**（`.cursor/skills/yukkuri-kyopro-chapter/`）を使います。依頼例: `@yukkuri-kyopro-chapter docs/01.md を執筆してください`。
