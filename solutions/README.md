# solutions

本文（`docs/NN.md`）からリンクする **解答例・サンプルコード** を置くディレクトリです。

## ディレクトリ規則

```
solutions/
  python/{章番号}/{問題ID}/main.py
  go/{章番号}/{問題ID}/main.go
```

| プレースホルダ | 意味 | 例 |
|----------------|------|-----|
| `{章番号}` | `docs/NN.md` の **NN**（Part 番号と一致） | `01` = [docs/01.md](../docs/01.md)（灰色） |
| `{問題ID}` | AtCoder 問題のスラッグ | `abc200_a` |

- 1 問題 1 ディレクトリを基本とする。
- ファイル名は言語ごとに `main.py` / `main.go`（複数解法がある場合は `main_fast.go` などサフィックス可）。

## 本文との対応

各 Part のディレクトリにある `README.md` に、解答の一覧と、そのコードを解説している本文の節を載せています。

| docs | Part | Python | Go |
|------|------|--------|----|
| [00.md](../docs/00.md) | はじめに | [python/00/](python/00/) | [go/00/](go/00/) |
| [01.md](../docs/01.md) | 灰色 | [python/01/](python/01/) | [go/01/](go/01/) |
| [02.md](../docs/02.md) | 茶色 | [python/02/](python/02/) | [go/02/](go/02/) |
| [03.md](../docs/03.md) | 緑 | [python/03/](python/03/) | [go/03/](go/03/) |
| [04.md](../docs/04.md) | 水色 | [python/04/](python/04/) | [go/04/](go/04/) |
| [05.md](../docs/05.md) | 青 | [python/05/](python/05/) | [go/05/](go/05/) |
| [06.md](../docs/06.md) | 黄色 | [python/06/](python/06/) | [go/06/](go/06/) |
| [07.md](../docs/07.md) | 橙色 | [python/07/](python/07/) | [go/07/](go/07/) |
| [08.md](../docs/08.md) | 赤 | [python/08/](python/08/) | [go/08/](go/08/) |

## テスト

- テンプレートと、本文で解説した ARC / AGC の解答は、小さいランダム入力で **愚直解と比べるテスト** があります（`tests/`、Go は各ディレクトリの `main_test.go`）。
- 同じディレクトリの Python 版と Go 版は、同じ入力に同じ出力を返します（`tests/test_py_go_parity.py`）。
- 実行方法はリポジトリ直下の [README.md](../README.md) を参照してください。

AtCoder から取得したローカルテストデータは **リポジトリに含めない**。入力例 1 だけを `input.txt` として置いています。
