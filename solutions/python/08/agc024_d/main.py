import sys
from collections import deque


def main() -> None:
    data = sys.stdin.read().split()
    n = int(data[0])
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = int(data[1 + 2 * i]) - 1, int(data[2 + 2 * i]) - 1
        g[a].append(b)
        g[b].append(a)

    def levels(roots):
        """roots（中心の頂点 1 つ、または中心の辺の両端）から BFS し、
        (最大の深さ, 各深さでの「子の数」の最大値のリスト) を返す"""
        dist = [-1] * n
        q = deque()
        for r in roots:
            dist[r] = 0
            q.append(r)
        max_children = []
        while q:
            v = q.popleft()
            ch = [to for to in g[v] if dist[to] == -1]
            d = dist[v]
            while len(max_children) <= d:
                max_children.append(0)
            max_children[d] = max(max_children[d], len(ch))
            for to in ch:
                dist[to] = d + 1
                q.append(to)
        return max(dist), max_children

    # 色の数の最小は「直径の半分 + 1」。直径上の頂点は、対称な位置どうし以外は同じ色にできないため。
    # 葉の数を最小にするには、中心（頂点 1 つ、または辺 1 本）から見て、同じ深さの頂点の子の数を
    # すべてその深さの最大にそろえる。葉の数はその積（辺が中心なら左右で 2 倍）
    best = None
    for c in range(n):  # 頂点が中心
        depth, mc = levels([c])
        leaves = 1
        for x in mc:
            if x:
                leaves *= x
        cand = (depth + 1, leaves)
        best = cand if best is None else min(best, cand)
    for u in range(n):  # 辺が中心
        for v in g[u]:
            if u < v:
                depth, mc = levels([u, v])
                leaves = 2
                for x in mc:
                    if x:
                        leaves *= x
                cand = (depth + 1, leaves)
                best = min(best, cand)
    print(*best)


if __name__ == "__main__":
    main()
