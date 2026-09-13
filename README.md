# yukkuri-kyopro

AtCoder（ABC / ARC / AGC）を土台に、レーティング帯ごとに競技プログラミングを学ぶ **ゆっくり解説** 付きハンズオン教材です。  
解説は **ゆっくり霊夢** と **ゆっくり魔理沙** の掛け合い形式。解答例は **Python** と **Go** の両方を掲載します。

> **非公式プロジェクト**です。東方 Project およびゆっくり関連の権利は各権利者に帰属します。

## 目次

**[docs/00-toc.md](docs/00-toc.md)** に全編の目次があります。

| ファイル | 内容 |
|----------|------|
| [docs/00.md](docs/00.md) | はじめに |
| [docs/01.md](docs/01.md)〜[08.md](docs/08.md) | 灰色〜赤色（Part 1〜8） |
| [docs/09.md](docs/09.md)〜[15.md](docs/15.md) | 付録 |

## 読み方

1. [docs/00-toc.md](docs/00-toc.md) で全体像を把握する。
2. 自分の AtCoder レーティングに近い Part（[docs/01.md](docs/01.md) 以降）から読む。前の Part は復習用でスキップしてよい。
3. 各 Part 内は **解説 → ハンズオン → まとめ演習** の順を推奨。
4. コードは本文ではなく [solutions/](solutions/) を参照し、Python と Go を見比べる。

## リポジトリ構成

```
docs/           # 本文（00-toc.md = 目次、00.md〜 = 各 Part）
solutions/
  python/       # 章番号ごと（例: 02/ = docs/01.md に対応）
  go/
scripts/        # ローカル検証用（任意）
```

- **ファイル番号と Part**: `docs/NN.md` の **NN** が Part 番号と一致（例: `00.md` = Part 0、`01.md` = Part 1 灰色）。
- **解答の置き場**: `solutions/python/01/abcxxx_a/main.py` のように、章番号 → 問題 ID → ファイル。

詳細は [solutions/README.md](solutions/README.md) を参照。

## 解答コードの実行

### Python

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"     # テスト実行時のみ

# 例: Part 0 の A+B を実行
python3 solutions/python/00/aplusb/main.py < solutions/python/00/aplusb/input.txt
```

### Go

```bash
go run ./solutions/go/00/aplusb/ < solutions/python/00/aplusb/input.txt
```

入出力は AtCoder 形式（標準入力 → 標準出力）を想定しています。

## 執筆（Cursor Agent）

章の執筆・`solutions/` 同期はプロジェクトスキル **yukkuri-kyopro-chapter**（`.cursor/skills/yukkuri-kyopro-chapter/`）を使う。依頼例: `@yukkuri-kyopro-chapter docs/01.md を執筆してください`。

## 開発メモ

| 項目 | 場所 |
|------|------|
| 目次・章立て | [docs/00-toc.md](docs/00-toc.md) |
| 問題と章の対応 | [docs/12.md](docs/12.md) |
| スニペット | [docs/11.md](docs/11.md) |

ローカルで AtCoder の問題を試すときは [AtCoder CLI](https://github.com/TatianaAtCoder/atcoder-cli) や [online-judge-tools](https://github.com/kmyk/online-judge-tools) を使い、生成されたテストデータや `contests/` ディレクトリは **コミットしない**（`.gitignore` 済み）。

## ライセンス

本リポジトリの文書・コードの利用条件は **[LICENSE](LICENSE)** に記載しています（著作権者: Hiromichi NOMATA）。
