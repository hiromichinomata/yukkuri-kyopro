import sys

sys.setrecursionlimit(10**7)


def main() -> None:
    n = 7
    g = [[] for _ in range(n)]
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    LOG = 4
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n

    def dfs(v, p):
        up[v][0] = p
        for i in range(1, LOG):
            if up[v][i - 1] != -1:
                up[v][i] = up[up[v][i - 1]][i - 1]
        for to in g[v]:
            if to == p:
                continue
            depth[to] = depth[v] + 1
            dfs(to, v)

    dfs(0, -1)

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        d = depth[a] - depth[b]
        for i in range(LOG):
            if d >> i & 1:
                a = up[a][i]
        if a == b:
            return a
        for i in range(LOG - 1, -1, -1):
            if up[a][i] != up[b][i]:
                a = up[a][i]
                b = up[b][i]
        return up[a][0]

    print(lca(3, 5), lca(4, 6))


if __name__ == "__main__":
    main()
