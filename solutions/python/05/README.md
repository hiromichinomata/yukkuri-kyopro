# Part 5（[docs/05.md](../../../docs/05.md)）— Python

青の Part の解答・テンプレートです。「本文」列は、そのコードを解説している節です。

| ディレクトリ | 内容 | 本文 |
|--------------|------|------|
| [abc214_f/](abc214_f/) | abc214_f（部分列の数え上げ DP（ABC F）） | [5.10](../../../docs/05.md#510-青色まとめハンズオン) |
| [abc229_d/](abc229_d/) | abc229_d（尺取り法） | [5.10](../../../docs/05.md#510-青色まとめハンズオン) |
| [abc240_f/](abc240_f/) | abc240_f（ランレングス + 数式） | [5.10](../../../docs/05.md#510-青色まとめハンズオン) |
| [abc256_d/](abc256_d/) | abc256_d（ソート・区間の併合） | [5.10](../../../docs/05.md#510-青色まとめハンズオン) |
| [agc004_a/](agc004_a/) | agc004_a（偶奇の考察） | [5.10](../../../docs/05.md#510-青色まとめハンズオン) |
| [arc146_b/](arc146_b/) | arc146_b（上のビットから貪欲（ARC B）） | [5.10](../../../docs/05.md#510-青色まとめハンズオン) |
| [arc151_b/](arc151_b/) | arc151_b（Union-Find + 数え上げ（ARC B）） | [5.10](../../../docs/05.md#510-青色まとめハンズオン) |
| [arc170_b/](arc170_b/) | arc170_b（考察（短い区間に必ずある）+ 全探索（ARC B）） | [5.10](../../../docs/05.md#510-青色まとめハンズオン) |
| [bipartite_matching/](bipartite_matching/) | 二部マッチング（最大流の特別な形） | [5.4](../../../docs/05.md#54-フロー入門二部マッチング) |
| [ccw/](ccw/) | CCW | [5.7](../../../docs/05.md#57-座標幾何入門) |
| [construction/](construction/) | 例題: 隣の差がすべて異なる順列 | [5.9](../../../docs/05.md#59-構築考察入門) |
| [convex_hull/](convex_hull/) | 凸包（Andrew の monotone chain） | [5.7](../../../docs/05.md#57-座標幾何入門) |
| [grundy/](grundy/) | Grundy 数（入門） | [5.5](../../../docs/05.md#55-ゲーム理論nim) |
| [kmp/](kmp/) | KMP | [5.6](../../../docs/05.md#56-文字列ローリングハッシュkmpz-アルゴリズム) |
| [kruskal/](kruskal/) | 計算量 | [5.1](../../../docs/05.md#51-最小全域木クラスカル) |
| [lcs/](lcs/) | LCS（O(NM)） | [5.2](../../../docs/05.md#52-最長共通部分列最長増加部分列応用) |
| [lis_fast/](lis_fast/) | LIS（O(N log N)） | [5.2](../../../docs/05.md#52-最長共通部分列最長増加部分列応用) |
| [max_flow/](max_flow/) | 増加路 BFS（入門） | [5.4](../../../docs/05.md#54-フロー入門二部マッチング) |
| [probability_dp/](probability_dp/) | 期待値 | [5.8](../../../docs/05.md#58-確率期待値-dp) |
| [rolling_hash/](rolling_hash/) | ローリングハッシュ（部分文字列を O(1) で比較） | [5.6](../../../docs/05.md#56-文字列ローリングハッシュkmpz-アルゴリズム) |
| [segtree_lazy/](segtree_lazy/) | 計算量 | [5.3](../../../docs/05.md#53-セグメント木応用-lazy-propagation) |
| [z_algorithm/](z_algorithm/) | Z アルゴリズム | [5.6](../../../docs/05.md#56-文字列ローリングハッシュkmpz-アルゴリズム) |

```bash
python3 solutions/python/05/abc214_f/main.py < solutions/python/05/abc214_f/input.txt
```

## 解き方のメモ（本文で解説していない問題）

本文の表にだけ載せている問題の方針です。まず自分で考えてから読んでください。

- **[abc214_f](https://atcoder.jp/contests/abc214/tasks/abc214_f)**（[abc214_f/](abc214_f/)）: 同じ文字列を二重に数えないよう、各文字列を「できるだけ左の位置で選ぶ」選び方だけを数える。dp[i] を「最後に選んだ文字が位置 i」とし、隣は選べないことと、もっと左で選べる場合を打ち切ることに注意する。
- **[abc229_d](https://atcoder.jp/contests/abc229/tasks/abc229_d)**（[abc229_d/](abc229_d/)）: 尺取り法。区間 [left, right] の「.」の数が K 以下になるように左端を進め、区間の長さの最大を取る。
- **[abc240_f](https://atcoder.jp/contests/abc240/tasks/abc240_f)**（[abc240_f/](abc240_f/)）: ランレングスの塊ごとに、B と A の変化を式で計算する。x < 0 の塊では B が正の間だけ A が増えるので、塊の中で A が最大になる位置を式で求めて候補にする。
- **[abc256_d](https://atcoder.jp/contests/abc256/tasks/abc256_d)**（[abc256_d/](abc256_d/)）: 区間を左端の順にソートし、今の区間と重なる（接する）間は右端を伸ばして併合する。
- **[agc004_a](https://atcoder.jp/contests/agc004/tasks/agc004_a)**（[agc004_a/](agc004_a/)）: どれかの辺が偶数なら半分に切れて差は 0。全部奇数なら、差は切り口の面積になるので、2 辺の積の最小。
- **[arc151_b](https://atcoder.jp/contests/arc151/tasks/arc151_b)**（[arc151_b/](arc151_b/)）: 置換 P のサイクルの数 c を Union-Find で数える。A = A∘P になるのは M^c 通りで、残りの M^N − M^c 通りは対称性で「A < A∘P」と「A > A∘P」に半分ずつ分かれる。
