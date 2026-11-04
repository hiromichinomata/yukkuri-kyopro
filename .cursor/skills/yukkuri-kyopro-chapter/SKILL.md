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
- [ ] 4. コードブロック（本文: 解説 + Python + Go 全文。solutions 同期）
- [ ] 4b. リライト時: コードブロック数が減っていないか確認
- [ ] 5. solutions/python/NN/ と solutions/go/NN/
- [ ] 6. 本文から solutions へのリンク
- [ ] 7. 正しさの確認（下の「正しさの確認」をすべて）
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
- 表の「想定スキル」は **AtCoder の問題文を実際に読んで** 書く。記憶や問題番号からの推測で書かない（過去に半数近くが実際の問題と食い違っていた）
- 目次の「コンテスト目安」（ABC / ARC / AGC）を表で触れる

### Step 4: コード（本文は多め）

- **Python と Go の両方**を載せる（片方だけの節を作らない）
- 本文にコードブロックを多めに置く（テンプレ・入出力・解法の骨格）
- 長い解答・再利用テンプレは `solutions/` に置き、本文は要所 + リンク

#### 解説と実装のバランス（必須）

**解説を厚くする依頼でも、実装ブロックは削らない。** コードだけの節・コメントだけの Go スケルトンに置き換えるのは禁止。

各アルゴリズム / データ構造の節は、だいたい次の順で書く:

1. **ゆっくり対談**（霊夢の疑問 → 魔理沙の説明）
2. **概念解説**（見出し `###` で区切ってよい）
   - イメージ・手順（番号付き）
   - **いつ使うか**（問題文のキーワード ↔ 手法の表）
   - **計算量**の目安
   - **つまずき**（off-by-one、逆順 DP、再帰深度など）
   - 前後 Part への橋渡し（例: 「[02.md](02.md) の累積和と…」）
3. **Python** の提出用テンプレ（関数ごとコピー可能な長さ）
4. **Go** の提出用テンプレ（**省略せず全文**。ヒープ・DSU など長くても本文に載せる）
5. `→ solutions/python/NN/...` / `go/...` リンク

| やってはいけない置き換え | 代わりに |
|--------------------------|----------|
| `// 4 近傍を見て…` だけの Go | ループまで書いた Go ブロック |
| 「solutions を参照」とだけ書いて本文にコードなし | 本文コード + solutions リンクの両方 |
| 解説追加のついでに Python/Go を 1 言語だけにする | 両言語を維持 |

解説追加・リライト時は、**変更前のコードブロック数（Python/Go 各）を数え**、減っていないか確認する。

参考（解説 + 実装の両立例）: [docs/03.md](../../../docs/03.md)

言語ルール:

| | Python | Go |
|---|--------|-----|
| 入出力 | `sys.stdin` / `input = sys.stdin.readline` | `bufio.NewReader(os.Stdin)` + `Writer` + `Flush` |
| 再帰 DFS | `sys.setrecursionlimit(10**7)` を必要なら明記。深い再帰は遅い（特に PyPy） | スタックは自動で伸びる（上限 1GB）ので、深さ 10^6 程度なら再帰のままでよい |
| 定数 | `INF = 10**18`, `MOD = 998244353` | `const inf int64 = 1 << 60` など |
| 提出 | デバッグ `print` は stderr 例のみ、提出用に残さない旨を書く | 同左 |
| 出力 | AtCoder 形式: 列は `print(*xs)`、真偽は `Yes` / `No`、小数は桁数固定 | 列は空白区切り（`strings.Trim(fmt.Sprint(xs), "[]")` など）。Python 版と同じ出力にする |

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
→ [solutions/python/NN/<dir>/](../solutions/python/NN/<dir>/) / [solutions/go/NN/<dir>/](../solutions/go/NN/<dir>/)
```

（`docs/NN.md` からの相対パスなので `../solutions/`。ブログに載せるときは `scripts/export_blog.py` で絶対 URL に変換する。運用の情報は [CONTRIBUTING.md](../../../CONTRIBUTING.md) に書き、README・本文には書かない）

実行例:

```bash
python3 solutions/python/NN/.../main.py < solutions/python/NN/.../input.txt
go run ./solutions/go/NN/.../ < solutions/python/NN/.../input.txt
```

### Step 7: 正しさの確認（必須）

過去の見直しで、問題 ID 名の解答の多くが **別の問題を解いていた**、テンプレートに **愚直解と比べれば分かるバグ** があった、本文のコードが **解答と食い違っていた**、という事故が見つかっている。次をすべて満たすまで完了にしない。

| 対象 | 確認すること | どこで |
|------|--------------|--------|
| 問題 ID 名の解答（`abc200_a/` など） | AtCoder の問題文を読み、**公式サンプルをすべて** Python・Go で通す | 手元で実行（サンプルはコミットしない。`input.txt` は入力例 1 のみ） |
| テンプレート（データ構造・アルゴリズム） | 小さいランダム入力で **愚直解（全探索）と比較** | Python: `tests/test_templates.py`、Go: 同ディレクトリの `main_test.go` |
| 本文で解説した ARC / AGC の解答 | 愚直解（構築問題は出力チェッカー）と比較 | `tests/test_problems.py` |
| 本文のコードブロック | 解答と同じコードであること。本文の Python ブロックは自動でテストにかかる | `tests/test_docs_code.py`（本文の節から `solutions/python/NN/<dir>/` へリンクしておく） |
| Python 版と Go 版 | 同じ入力（`input.txt`、なければ空）に **同じ出力** | `tests/test_py_go_parity.py` |
| リンク | 相対リンク・アンカー（`#見出し`）が切れていない | `tests/test_links.py` |

本文のコードは手で写さず、**テスト済みの `solutions/` のファイルから貼る**（関数・クラス部分を切り出す）。

```bash
python3 -m pytest                  # すべて（Python と Go の出力比較で 1 分ほど）
python3 -m pytest -m "not parity"  # 出力比較を除いて手早く
go vet ./... && go test ./solutions/go/...
gofmt -l solutions/go              # 何も出なければ OK
```

### Step 8: 問題索引

推奨問題を書いたら [docs/12.md](../../../docs/12.md) に行追加:

`| NN | 節 | 問題 ID | メモ |`

## やってはいけないこと

- AtCoder 問題文の **全文転載**
- `oj` / `acc` で落とした **非公開テストデータ**のコミット
- `solutions/` だけ更新して **docs のリンク・説明を放置**
- 霊夢・魔理沙以外のキャラをメイン解説にする（本書は二人のみ）
- 問題 ID 名のディレクトリ（`abc088_b/` など）に、**その問題ではない練習問題** の解答を置く（練習用は `simulate_left_only/` のようなトピック名にする）
- 「〜相当」と書いて、実在の問題 ID に架空の問題内容を結び付ける
- テストを通していないコードを本文に載せる
- 章番号と Part の取り違え（`docs/NN.md` の NN = Part 番号、`00.md` = Part 0）
- **解説を増やす名目で Python/Go 実装を削る・コメント化する**（両立が原則）

## 付録（09〜15）

- 対談は省略可。リファレンス・表・コード一覧中心
- [docs/11.md](../../../docs/11.md) スニペットは `solutions/` のテスト済みコードをそのまま集約する（独自の書き換え版を置かない）。Python / Go を並記し、各節に `solutions/python/NN/<dir>/` へのリンクを置く（`tests/test_docs_code.py` の対象になる）

## 参照

- ファイル番号・色・Part 対応: [reference.md](reference.md)
- 執筆済みの型: [docs/00.md](../../../docs/00.md)（入門）, [docs/02.md](../../../docs/02.md)（茶色・解説厚め）, [docs/03.md](../../../docs/03.md)（緑・技法解説 + 実装両立）
- [solutions/python/00/](../../../solutions/python/00/)
