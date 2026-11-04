import sys

MOD = 998244353


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = int(data[2 + 2 * i]) - 1, int(data[3 + 2 * i]) - 1
        g[a].append(b)
        g[b].append(a)
    fac = [1] * (2 * n + 2)
    for i in range(1, 2 * n + 2):
        fac[i] = fac[i - 1] * i % MOD
    # 操作は「頂点の一様ランダムな順列の順に、K+1 頂点以上の成分にいる頂点だけを選ぶ」と同じ。
    # 期待値の線形性で、各頂点 v が選ばれる確率を足す。v が選ばれる ⇔ ある連結な集合 S ∋ v（|S| = s ≥ K+1）で、
    # S の外側に隣接する b 頂点がすべて v より前、S の残り s-1 頂点がすべて v より後 → 確率 b!(s-1)!/(s+b)!。
    # S ごとに v の選び方が s 通りあるので、連結な S を (s, b) ごとに数えればよい（木 DP）
    parent = [-1] * n
    order = [0]
    seen = [False] * n
    seen[0] = True
    for v in order:
        for to in g[v]:
            if not seen[to]:
                seen[to] = True
                parent[to] = v
                order.append(to)
    # dp[v][s][b]: v を「一番上」とする連結な S（v の部分木の中）で、大きさ s、部分木の中の境界 b 個の数
    dp = [None] * n
    total = 0
    for v in reversed(order):
        cur = {(1, 0): 1}
        for c in g[v]:
            if c == parent[v]:
                continue
            nxt = {}
            for (s1, b1), x in cur.items():
                key = (s1, b1 + 1)  # 子 c を S に入れない → c は境界
                nxt[key] = (nxt.get(key, 0) + x) % MOD
                for (s2, b2), y in dp[c].items():  # 子 c を S に入れる
                    key = (s1 + s2, b1 + b2)
                    nxt[key] = (nxt.get(key, 0) + x * y) % MOD
            cur = nxt
            dp[c] = None
        dp[v] = cur
        for (s, b), x in cur.items():
            if s >= k + 1:
                bb = b + (1 if parent[v] != -1 else 0)  # 親も境界
                p = fac[bb] * fac[s - 1] % MOD * pow(fac[s + bb], MOD - 2, MOD) % MOD
                total = (total + x * s % MOD * p) % MOD
    print(total)


if __name__ == "__main__":
    main()
