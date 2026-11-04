# Part 3（[docs/03.md](../../../docs/03.md)）— Python

緑の Part の解答・テンプレートです。「本文」列は、そのコードを解説している節です。

| ディレクトリ | 内容 | 本文 |
|--------------|------|------|
| [abc084_d/](abc084_d/) | abc084_d（篩 + 累積和） | [3.10](../../../docs/03.md#310-緑まとめハンズオン) |
| [abc126_c/](abc126_c/) | abc126_c（全探索・確率） | [3.10](../../../docs/03.md#310-緑まとめハンズオン) |
| [abc129_c/](abc129_c/) | abc129_c（階段の上り方 DP） | [3.4](../../../docs/03.md#34-動的計画法入門) |
| [abc137_d/](abc137_d/) | abc137_d（貪欲 + ヒープ） | [3.9](../../../docs/03.md#39-優先度付きキューダイクストラ入門) |
| [abc146_c/](abc146_c/) | abc146_c（答えの二分探索） | [3.2](../../../docs/03.md#32-二分探索) |
| [abc156_d/](abc156_d/) | abc156_d（組合せ mod） | [3.10](../../../docs/03.md#310-緑まとめハンズオン) |
| [abc172_d/](abc172_d/) | abc172_d（約数の個数（倍数側から数える）） | [3.10](../../../docs/03.md#310-緑まとめハンズオン) |
| [abc177_d/](abc177_d/) | abc177_d（Union-Find・最大成分） | [3.6](../../../docs/03.md#36-union-finddsu) |
| [abc183_c/](abc183_c/) | abc183_c（順列全探索） | [3.10](../../../docs/03.md#310-緑まとめハンズオン) |
| [abc213_c/](abc213_c/) | abc213_c（座標圧縮） | [3.10](../../../docs/03.md#310-緑まとめハンズオン) |
| [abc214_d/](abc214_d/) | abc214_d（辺のソート + Union-Find） | [3.10](../../../docs/03.md#310-緑まとめハンズオン) |
| [abc222_c/](abc222_c/) | abc222_c（ソート・シミュレーション） | [3.10](../../../docs/03.md#310-緑まとめハンズオン) |
| [arc104_a/](arc104_a/) | arc104_a（連立方程式（易しい ARC A）） | [3.10](../../../docs/03.md#310-緑まとめハンズオン) |
| [binary_search_answer/](binary_search_answer/) | 答えの二分 | [3.2](../../../docs/03.md#32-二分探索) |
| [deque_window/](deque_window/) | スライディングウィンドウ（deque） | [3.3](../../../docs/03.md#33-スタックキューdeque) |
| [dijkstra/](dijkstra/) | ダイクストラの流れ | [3.9](../../../docs/03.md#39-優先度付きキューダイクストラ入門) |
| [dp_paths/](dp_paths/) | 経路数（右・下のみ） | [3.4](../../../docs/03.md#34-動的計画法入門) |
| [dsu/](dsu/) | DSU | [3.6](../../../docs/03.md#36-union-finddsu) |
| [graph_adj_list/](graph_adj_list/) | 無向・有向 | [3.5](../../../docs/03.md#35-グラフの基礎) |
| [grid_bfs/](grid_bfs/) | グリッド BFS | [3.1](../../../docs/03.md#31-深さ優先探索幅優先探索) |
| [grid_dfs/](grid_dfs/) | DFS で連結成分のサイズ | [3.1](../../../docs/03.md#31-深さ優先探索幅優先探索) |
| [knapsack/](knapsack/) | 01 ナップサック — なぜ逆順か | [3.4](../../../docs/03.md#34-動的計画法入門) |
| [kruskal/](kruskal/) | クラスカル（最小全域木の準備） | [3.6](../../../docs/03.md#36-union-finddsu) |
| [lis/](lis/) | LIS（最長増加部分列） | [3.4](../../../docs/03.md#34-動的計画法入門) |
| [lower_bound/](lower_bound/) | lower_bound 相当 | [3.2](../../../docs/03.md#32-二分探索) |
| [ncr/](ncr/) | パスカルの三角形 | [3.8](../../../docs/03.md#38-数学整数と組み合わせの基礎) |
| [prime_divisors/](prime_divisors/) | 素数判定・約数・素因数分解 | [3.8](../../../docs/03.md#38-数学整数と組み合わせの基礎) |
| [sieve/](sieve/) | エラトステネスの篩（1〜N の素数をまとめて） | [3.8](../../../docs/03.md#38-数学整数と組み合わせの基礎) |
| [stack_brackets/](stack_brackets/) | 括弧の対応（スタック） | [3.3](../../../docs/03.md#33-スタックキューdeque) |
| [topological_sort/](topological_sort/) | Kahn 法（入次数） | [3.7](../../../docs/03.md#37-トポロジカルソート) |
| [tree_dfs/](tree_dfs/) | 木（tree）の DFS | [3.5](../../../docs/03.md#35-グラフの基礎) |

```bash
python3 solutions/python/03/abc084_d/main.py < solutions/python/03/abc084_d/input.txt
```

## 解き方のメモ（本文で解説していない問題）

本文の表にだけ載せている問題の方針です。まず自分で考えてから読んでください。

- **[abc084_d](https://atcoder.jp/contests/abc084/tasks/abc084_d)**（[abc084_d/](abc084_d/)）: エラトステネスの篩で素数を求め、「x も (x + 1) / 2 も素数」になる奇数 x の個数を累積和にしておく。各クエリは差を取って O(1)。
- **[abc126_c](https://atcoder.jp/contests/abc126/tasks/abc126_c)**（[abc126_c/](abc126_c/)）: サイコロの目ごとに、得点が K 以上になるまでに必要な表の回数を数え、その確率 (1/2)^回数 を足して N で割る。
- **[abc156_d](https://atcoder.jp/contests/abc156/tasks/abc156_d)**（[abc156_d/](abc156_d/)）: 花束の作り方は全部で 2^n − 1 通り。そこから a 本と b 本の作り方 C(n, a)、C(n, b) を引く。n が大きく a, b が小さいので、C(n, r) は n(n − 1)…(n − r + 1) / r! を mod で計算する。
- **[abc172_d](https://atcoder.jp/contests/abc172/tasks/abc172_d)**（[abc172_d/](abc172_d/)）: 主客転倒。K × f(K) の和は、各 d について「d の倍数 K」の和 d × m(m + 1) / 2（m = N // d）を足したものに等しい。O(N)。
- **[abc183_c](https://atcoder.jp/contests/abc183/tasks/abc183_c)**（[abc183_c/](abc183_c/)）: 都市 1 を始点・終点に固定し、残りの N − 1 都市を回る順番を順列全探索する。移動時間の合計がちょうど K の順番を数える。
- **[abc213_c](https://atcoder.jp/contests/abc213/tasks/abc213_c)**（[abc213_c/](abc213_c/)）: 数字のある行・列だけが残るので、行番号と列番号をそれぞれ座標圧縮すればよい。
- **[abc214_d](https://atcoder.jp/contests/abc214/tasks/abc214_d)**（[abc214_d/](abc214_d/)）: 辺を重みの小さい順に Union-Find でつなぐ。辺 (u, v, w) をつないだ瞬間に初めて行き来できる組は両側の成分の大きさの積だけあり、その組の値はちょうど w（主客転倒）。
- **[abc222_c](https://atcoder.jp/contests/abc222/tasks/abc222_c)**（[abc222_c/](abc222_c/)）: ラウンドごとに、順位の隣どうしでじゃんけんの勝敗を決め、「勝ち数の多い順、同じなら番号の小さい順」に並べ直す。問題文どおりのシミュレーション。
- **[arc104_a](https://atcoder.jp/contests/arc104/tasks/arc104_a)**（[arc104_a/](arc104_a/)）: X + Y = A、X − Y = B を解くと X = (A + B) / 2、Y = (A − B) / 2。
