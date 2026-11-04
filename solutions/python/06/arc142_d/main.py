import sys

MOD = 998244353


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = int(data[1 + 2 * i]) - 1, int(data[2 + 2 * i]) - 1
        g[a].append(b)
        g[b].append(a)
    # 条件を満たす置き方は、頂点全体を「2 頂点以上のパス」に分け、各パスの片方の端だけ駒を置かない形。
    # パスどうしをつなぐ辺は「端点どうし」か「内部の頂点どうし」だけが許され、
    # 内部どうしの辺 1 本ごとに、両側の向き（どちらの端を空けるか）を独立に選べる（× 2）。
    # 木 DP の状態（頂点 v の部分木について）:
    #   up[v]: v のパスが親へ続く
    #   ce[v]: v のパスが部分木内で閉じ、v はその端点
    #   ci[v]: v のパスが部分木内で閉じ、v はその内部の頂点
    parent = [-1] * n
    order = [0]
    parent[0] = n  # 番兵
    for v in order:
        for to in g[v]:
            if parent[to] == -1:
                parent[to] = v
                order.append(to)
    up, ce, ci = [0] * n, [0] * n, [0] * n
    for v in reversed(order):
        # e0/e1: 子をすべて「端点で閉じた」とつなぐ（v が端点のとき）。e1 は 1 つだけ「パスが v へ続く」子を含む
        # i0/i1/i2: 子をすべて「内部で閉じた」とつなぐ（v が内部のとき、× 2）。i1・i2 は続く子が 1・2 個
        e0, e1 = 1, 0
        i0, i1, i2 = 1, 0, 0
        for c in g[v]:
            if c == parent[v]:
                continue
            u, x, y = up[c], ce[c], 2 * ci[c] % MOD
            e0, e1 = e0 * x % MOD, (e1 * x + e0 * u) % MOD
            i0, i1, i2 = i0 * y % MOD, (i1 * y + i0 * u) % MOD, (i2 * y + i1 * u) % MOD
        up[v] = (e0 + i1) % MOD  # v が端点で親へ続く ＋ v が内部で、子 1 つから来て親へ続く
        ce[v] = e1  # v が端点で、子 1 つへ続いて閉じる
        ci[v] = i2  # v が内部で、子 2 つを通って閉じる
    # 根のパスの向き 2 通り（内部どうしの辺の分はすでに掛けてある）
    print(2 * (ce[0] + ci[0]) % MOD)


if __name__ == "__main__":
    main()
