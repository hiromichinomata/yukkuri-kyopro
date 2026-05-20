---
name: yukkuri-kyopro-chapter
description: >-
  Writes and syncs yukkuri-kyopro book chapters (docs/NN.md, solutions in
  Python/Go, Yukkuri Reimu/Marisa dialogue). Use when authoring or editing a
  chapter, Part, docs/00.md–15.md, 執筆, ゆっくり解説, 競プロ教材, or syncing
  solutions with chapter text.
---

# yukkuri-kyopro 章執筆

AtCoder ベースの競プロ教材。**ゆっくり霊夢**（初学者）と **ゆっくり魔理沙**（解説）の対談で `docs/NN.md` を書き、**Python / Go** のコードを `solutions/` に同期する。

## 着手前

1. 対象ファイル番号 `NN` を確定（[reference.md](reference.md) の対応表）
2. [docs/00-toc.md](../../../docs/00-toc.md) でその Part の節一覧・到達目標・コンテスト目安を読む
3. 既存の [docs/NN.md](../../../docs/NN.md) と **前の章**（`NN-1`）を読み、トーンと難易度を揃える
4. 付録のみ（`09`〜`15`）のときは [docs/00.md](../../../docs/00.md) のコード方針を参照し、対談形式は省略可

## 執筆ワークフロー

```
Task Progress:
- [ ] 0. 目次・前章を確認
- [ ] 1. docs/NN.md の骨組み（見出し・ナビ・到達チェック）
- [ ] 2. ゆっくり対談（📖 各節）
- [ ] 3. ハンズオン（🖐️）と 🎯 まとめ
- [ ] 4. コードブロック（本文多め + solutions 同期）
- [ ] 5. solutions/python/NN/ と solutions/go/NN/
- [ ] 6. 本文から solutions へのリンク
- [ ] 7. 実行・テスト（動くものだけ）
- [ ] 8. 問題索引 docs/12.md を更新（推奨問題を書いた場合）
```

### Step 1: `docs/NN.md` の骨組み

必須要素:

- タイトル `# Part X — …` または `# 付録 …`
- 冒頭 1〜2 行の概要
- **リポジトリ上のコード** 表（Part 本文がある場合）→ `solutions/python/NN/`, `solutions/go/NN/`
- ナビ: `← [目次](00-toc.md) | 次 → [MM.md](MM.md)（次章名）`
- 各節は目次の番号に合わせる（例: `## 1.1 …` は Part 1 / `01.md` 用）

末尾:

- **到達チェック**（チェックリスト）
- **まとめ** 表（任意だが推奨）
- ナビの繰り返し

### Step 2: ゆっくり対談

| キャラ | 役割 |
|--------|------|
| **霊夢** | 初見の疑問・誤解・「つまずき」の代弁 |
| **魔理沙** | 定義・手順・競プロのコツ・次のアクション |

形式（厳守）:

```markdown
**霊夢**: 〜？

**魔理沙**: 〜。
```

- 1 節の流れ: 霊夢の疑問 → 魔理沙の説明 →（必要なら）霊夢の確認 → 魔理沙の補足
- アルゴリズム名は初出で短く定義する
- 非公式・東方/ゆっくり権利は **Part 0 または README で既出** なら繰り返しすぎない

### Step 3: ハンズオンと問題

- 🖐️ 節: 手順番号・ローカル実行コマンド・期待出力
- 🎯 節: AtCoder 問題を **ID 付き**で列挙（例: `abc200_a`）。問題文の全文転載はしない
- 目次の「コンテスト目安」（ABC / ARC / AGC）を表で触れる

### Step 4: コード（本文は多め）

- **Python と Go の両方**を載せる（片方だけの節を作らない）
- 本文にコードブロックを多めに置く（テンプレ・入出力・解法の骨格）
- 長い解答・再利用テンプレは `solutions/` に置き、本文は要所 + リンク

言語ルール:

| | Python | Go |
|---|--------|-----|
| 入出力 | `sys.stdin` / `input = sys.stdin.readline` | `bufio.NewReader(os.Stdin)` + `Writer` + `Flush` |
| 再帰 DFS | `sys.setrecursionlimit(10**7)` を必要なら明記 | 深い再帰は注意、スタック/ループ代替に言及 |
| 定数 | `INF = 10**18`, `MOD = 998244353` | `const inf int64 = 1 << 60` など |
| 提出 | デバッグ `print` は stderr 例のみ、提出用に残さない旨を書く | 同左 |

### Step 5: `solutions/` の同期

配置規則（[solutions/README.md](../../../solutions/README.md)）:

```
solutions/python/{NN}/{topic_or_problem_id}/main.py
solutions/go/{NN}/{topic_or_problem_id}/main.go
```

| 種類 | 例 |
|------|-----|
| テンプレ | `template/main.py` |
| ハンズオン | `aplusb/`, `abc200_a/` |
| サンプル入力 | 同ディレクトリの `input.txt`（小さいもののみ） |

各 `solutions/python/{NN}/` と `solutions/go/{NN}/` に **README.md**（ディレクトリ一覧）を置く。

### Step 6: 本文リンク

テンプレ・ハンズオンの節に追記:

```markdown
→ [solutions/python/NN/.../main.py](../../../solutions/python/NN/.../main.py)
```

実行例:

```bash
python3 solutions/python/NN/.../main.py < solutions/python/NN/.../input.txt
go run ./solutions/go/NN/.../ < solutions/python/NN/.../input.txt
```

### Step 7: 検証

```bash
python3 solutions/python/NN/<dir>/main.py < solutions/python/NN/<dir>/input.txt
go run ./solutions/go/NN/<dir>/
go test ./solutions/go/NN/<dir>/   # テストを書いた場合
pytest solutions/python/NN/<dir>/  # test_*.py がある場合
```

### Step 8: 問題索引

推奨問題を書いたら [docs/12.md](../../../docs/12.md) に行追加:

`| NN | 節 | 問題 ID | メモ |`

## やってはいけないこと

- AtCoder 問題文の **全文転載**
- `oj` / `acc` で落とした **非公開テストデータ**のコミット
- `solutions/` だけ更新して **docs のリンク・説明を放置**
- 霊夢・魔理沙以外のキャラをメイン解説にする（本書は二人のみ）
- 章番号と Part の取り違え（`01.md` = Part 1 灰色、`00.md` = Part 0）

## 付録（09〜15）

- 対談は省略可。リファレンス・表・コード一覧中心
- [docs/11.md](../../../docs/11.md) スニペットは [solutions/python/00/](../../../solutions/python/00/) 等を再利用・集約してよい

## 参照

- ファイル番号・色・Part 対応: [reference.md](reference.md)
- 執筆済みの型: [docs/00.md](../../../docs/00.md), [solutions/python/00/](../../../solutions/python/00/)
