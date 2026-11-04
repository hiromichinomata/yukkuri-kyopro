# Part 4（[docs/04.md](../../../docs/04.md)）— Python

水色の Part の解答・テンプレートです。「本文」列は、そのコードを解説している節です。

| ディレクトリ | 内容 | 本文 |
|--------------|------|------|
| [abc035_c/](abc035_c/) | abc035_c（1 次元いもすの復習） | [4.2](../../../docs/04.md#42-二次元累積和いもす法) |
| [abc147_d/](abc147_d/) | abc147_d（ビットごとの寄与） | [4.9](../../../docs/04.md#49-期待値の線形性主客転倒) |
| [abc154_e/](abc154_e/) | abc154_e（桁 DP） | [4.4](../../../docs/04.md#44-桁-dp) |
| [abc180_e/](abc180_e/) | abc180_e（bitmask DP） | [4.10](../../../docs/04.md#410-水色まとめハンズオン) |
| [abc184_e/](abc184_e/) | abc184_e（BFS（テレポートは文字ごとに 1 回だけ使う）） | [4.1](../../../docs/04.md#41-最短経路) |
| [abc186_d/](abc186_d/) | abc186_d（ソート + 主客転倒） | [4.9](../../../docs/04.md#49-期待値の線形性主客転倒) |
| [abc187_e/](abc187_e/) | abc187_e（木の上の累積和） | [4.10](../../../docs/04.md#410-水色まとめハンズオン) |
| [abc194_d/](abc194_d/) | abc194_d（期待値） | [4.9](../../../docs/04.md#49-期待値の線形性主客転倒) |
| [abc199_d/](abc199_d/) | abc199_d（3 色塗りの数え上げ（DFS で全探索）） | [4.8](../../../docs/04.md#48-二分グラフ判定) |
| [arc115_a/](arc115_a/) | arc115_a（1 の個数の偶奇で分類（ARC A）） | [4.10](../../../docs/04.md#410-水色まとめハンズオン) |
| [arc118_a/](arc118_a/) | arc118_a（周期性・数式（ARC A）） | [4.10](../../../docs/04.md#410-水色まとめハンズオン) |
| [arc120_a/](arc120_a/) | arc120_a（累積和・累積 max（ARC A）） | [4.10](../../../docs/04.md#410-水色まとめハンズオン) |
| [bfs01/](bfs01/) | 0-1 BFS（deque） | [4.1](../../../docs/04.md#41-最短経路) |
| [bipartite/](bipartite/) | 計算量 | [4.8](../../../docs/04.md#48-二分グラフ判定) |
| [contribution/](contribution/) | つまずき | [4.9](../../../docs/04.md#49-期待値の線形性主客転倒) |
| [digit_dp/](digit_dp/) | 桁和が D の倍数になる数を数える | [4.4](../../../docs/04.md#44-桁-dp) |
| [dp_bitmask/](dp_bitmask/) | bitmask DP（小さな N） | [4.3](../../../docs/04.md#43-dp-の応用) |
| [dp_interval/](dp_interval/) | 区間 DP（例: 石の合体） | [4.3](../../../docs/04.md#43-dp-の応用) |
| [dp_s/](dp_s/) | 桁和が D の倍数になる数を数える | [4.4](../../../docs/04.md#44-桁-dp) |
| [dp_tree/](dp_tree/) | 木 DP（部分木の値） | [4.3](../../../docs/04.md#43-dp-の応用) |
| [fenwick/](fenwick/) | Fenwick | [4.5](../../../docs/04.md#45-セグメント木fenwick入門) |
| [floyd_warshall/](floyd_warshall/) | ワーシャル（全点対） | [4.1](../../../docs/04.md#41-最短経路) |
| [imos_2d/](imos_2d/) | 二次元いもす法（矩形にまとめて足す） | [4.2](../../../docs/04.md#42-二次元累積和いもす法) |
| [modinv/](modinv/) | つまずき | [4.7](../../../docs/04.md#47-数学逆元フェルマ) |
| [prefix_sum_2d/](prefix_sum_2d/) | 構築（1-indexed） | [4.2](../../../docs/04.md#42-二次元累積和いもす法) |
| [segtree/](segtree/) | セグメント木（区間和・一点更新） | [4.5](../../../docs/04.md#45-セグメント木fenwick入門) |
| [two_pointers/](two_pointers/) | 問題文のキーワード | [4.6](../../../docs/04.md#46-スライディングウィンドウ尺取り) |

```bash
python3 solutions/python/04/abc035_c/main.py < solutions/python/04/abc035_c/input.txt
```

## 解き方のメモ（本文で解説していない問題）

本文の表にだけ載せている問題の方針です。まず自分で考えてから読んでください。

- **[abc035_c](https://atcoder.jp/contests/abc035/tasks/abc035_c)**（[abc035_c/](abc035_c/)）: いもす法。区間 [l, r] を裏返すたびに差分配列に +1 と −1 を入れ、最後に累積和を取る。裏返した回数が奇数なら 1。
- **[abc147_d](https://atcoder.jp/contests/abc147/tasks/abc147_d)**（[abc147_d/](abc147_d/)）: ビットごとに考える。b ビット目が 1 になる組の数は「そのビットが 1 の数」×「0 の数」で、それぞれ 2^b ずつ寄与する。
- **[abc154_e](https://atcoder.jp/contests/abc154/tasks/abc154_e)**（[abc154_e/](abc154_e/)）: 桁 DP。dp[tight][c] を「上の桁から決めて、0 でない桁を c 個使った数の個数」（tight はここまで N と同じか）とし、ちょうど K 個のものを数える。
- **[abc180_e](https://atcoder.jp/contests/abc180/tasks/abc180_e)**（[abc180_e/](abc180_e/)）: 費用が三角不等式を満たすので、各都市をちょうど 1 回ずつ回る巡回でよい。bit DP（dp[mask][v]）で巡回セールスマン問題として解く。
- **[abc186_d](https://atcoder.jp/contests/abc186/tasks/abc186_d)**（[abc186_d/](abc186_d/)）: ソートしても、ペアの差の絶対値の和は変わらない。ソート後は a_j が「自分より前の j 個」との差で j 回足され、前の値の和が引かれるので、累積和で求まる。
- **[abc187_e](https://atcoder.jp/contests/abc187/tasks/abc187_e)**（[abc187_e/](abc187_e/)）: 頂点 1 を根にする。「辺の片側に足す」操作は、子の側なら「その部分木に足す」、親の側なら「根に足して、子の部分木から引く」と言い換え、最後に根から累積和を流す。
- **[abc194_d](https://atcoder.jp/contests/abc194/tasks/abc194_d)**（[abc194_d/](abc194_d/)）: 連結成分に k 頂点入っているとき、外の頂点を選ぶ確率は (N − k) / N。成功まで繰り返す回数の期待値は N / (N − k) なので、k = 1〜N − 1 で足す（期待値の線形性）。
- **[arc118_a](https://atcoder.jp/contests/arc118/tasks/arc118_a)**（[arc118_a/](arc118_a/)）: 税抜き A が 100 増えると、税込みはちょうど 100 + t 増える（周期性）。1 周期（A = 1〜100）で抜ける t 個の値を求め、N 番目を周期と余りから計算する。
- **[dp_s](https://atcoder.jp/contests/dp/tasks/dp_s)**（[dp_s/](dp_s/)）: 桁 DP。dp[tight][r] を「上の桁から決めて、桁和を D で割った余りが r の数の個数」とする。0 も数えてしまうので最後に 1 引く。
