# Part 2（[docs/02.md](../../../docs/02.md)）— Go

茶色の Part の解答・テンプレートです。「本文」列は、そのコードを解説している節です。

| ディレクトリ | 内容 | 本文 |
|--------------|------|------|
| [abc128_c/](abc128_c/) | abc128_c（bit 全探索） | [2.2](../../../docs/02.md#22-bit-全探索順列全探索) |
| [abc134_c/](abc134_c/) | abc134_c（自分以外の最大） | [2.9](../../../docs/02.md#29-茶色まとめハンズオン) |
| [abc136_c/](abc136_c/) | abc136_c（左から貪欲） | [2.3](../../../docs/02.md#23-貪欲法入門) |
| [abc142_b/](abc142_b/) | abc142_b（条件を満たす個数を数える） | [2.9](../../../docs/02.md#29-茶色まとめハンズオン) |
| [abc145_c/](abc145_c/) | abc145_c（順列全探索） | [2.2](../../../docs/02.md#22-bit-全探索順列全探索) |
| [abc146_b/](abc146_b/) | abc146_b（文字シフト） | [2.7](../../../docs/02.md#27-文字列処理) |
| [abc150_c/](abc150_c/) | abc150_c（順列の番号） | [2.2](../../../docs/02.md#22-bit-全探索順列全探索) |
| [abc151_c/](abc151_c/) | abc151_c（問題ごとに集計するシミュレーション） | [2.9](../../../docs/02.md#29-茶色まとめハンズオン) |
| [abc152_b/](abc152_b/) | abc152_b（辞書順の比較） | [2.7](../../../docs/02.md#27-文字列処理) |
| [abc153_b/](abc153_b/) | abc153_b（総和と比較） | [2.9](../../../docs/02.md#29-茶色まとめハンズオン) |
| [abc167_c/](abc167_c/) | abc167_c（bit 全探索 + 最小化） | [2.2](../../../docs/02.md#22-bit-全探索順列全探索) |
| [arc083_a/](arc083_a/) | arc083_a（水と砂糖の量を全列挙（旧 ARC、ABC C 相当）） | [2.9](../../../docs/02.md#29-茶色まとめハンズオン) |
| [bit_search/](bit_search/) | 和が K になる選び方を数える（bit 全探索） | [2.2](../../../docs/02.md#22-bit-全探索順列全探索) |
| [compress_coords/](compress_coords/) | 計算量 | [2.8](../../../docs/02.md#28-座標圧縮入門) |
| [counter_freq/](counter_freq/) | 頻度カウント | [2.6](../../../docs/02.md#26-集合辞書カウンタ) |
| [diff_array/](diff_array/) | 差分配列（区間に一括 +1） | [2.5](../../../docs/02.md#25-累積和差分1-次元) |
| [greedy_intervals/](greedy_intervals/) | 区間スケジューリング（終了時刻が早い順） | [2.3](../../../docs/02.md#23-貪欲法入門) |
| [grid_4dir/](grid_4dir/) | 4 方向への移動 | [2.4](../../../docs/02.md#24-二次元グリッド) |
| [permutation_search/](permutation_search/) | 全都市を回る最短距離（順列全探索） | [2.2](../../../docs/02.md#22-bit-全探索順列全探索) |
| [prefix_sum/](prefix_sum/) | 累積和 | [2.5](../../../docs/02.md#25-累積和差分1-次元) |
| [sort_pairs/](sort_pairs/) | 昇順・降順 | [2.1](../../../docs/02.md#21-ソートとカスタム比較) |

```bash
go run ./solutions/go/02/abc128_c/ < solutions/python/02/abc128_c/input.txt
```

## 解き方のメモ（本文で解説していない問題）

本文の表にだけ載せている問題の方針です。まず自分で考えてから読んでください。

- **[abc128_c](https://atcoder.jp/contests/abc128/tasks/abc128_c)**（[abc128_c/](abc128_c/)）: スイッチの on / off を 2^N 通り全部試し（bit 全探索）、すべての電球で「つながっている on のスイッチの数の偶奇」が条件どおりかを確かめる。
- **[abc134_c](https://atcoder.jp/contests/abc134/tasks/abc134_c)**（[abc134_c/](abc134_c/)）: 自分以外の最大値は、自分が最大値でなければ全体の最大値、自分が最大値なら 2 番目に大きい値。上位 2 つを持てば O(N)。
- **[abc142_b](https://atcoder.jp/contests/abc142/tasks/abc142_b)**（[abc142_b/](abc142_b/)）: 高さが K 以上の人を数えるだけ。
- **[abc145_c](https://atcoder.jp/contests/abc145/tasks/abc145_c)**（[abc145_c/](abc145_c/)）: 町を訪れる順番を順列全探索し（N ≤ 8 なので 8! = 40320 通り）、道のりの平均を取る。
- **[abc150_c](https://atcoder.jp/contests/abc150/tasks/abc150_c)**（[abc150_c/](abc150_c/)）: `itertools.permutations` は辞書順に列挙するので、P と Q が何番目に出てくるかを数えて差を取る。
- **[abc151_c](https://atcoder.jp/contests/abc151/tasks/abc151_c)**（[abc151_c/](abc151_c/)）: 問題ごとに「AC したか」と「最初の AC までの WA の数」を持つ。ペナルティには AC した問題の WA だけを足す。
- **[abc153_b](https://atcoder.jp/contests/abc153/tasks/abc153_b)**（[abc153_b/](abc153_b/)）: 必殺技を全部 1 回ずつ使うのが最大のダメージなので、総和が体力 H 以上かを判定する。
- **[abc167_c](https://atcoder.jp/contests/abc167/tasks/abc167_c)**（[abc167_c/](abc167_c/)）: どの参考書を買うかを 2^N 通り全部試し（bit 全探索）、すべての理解度が X 以上になる組の最小金額を取る（なければ -1）。
- **[arc083_a](https://atcoder.jp/contests/arc083/tasks/arc083_a)**（[arc083_a/](arc083_a/)）: 操作 1・2 で作れる水の量と、操作 3・4 で作れる砂糖の量をそれぞれ全部列挙し、溶け残りと容器の上限を守る組から濃度が最大のものを選ぶ。濃度は割り算せず、掛け算で比べる。
