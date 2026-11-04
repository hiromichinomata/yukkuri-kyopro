import sys

sys.setrecursionlimit(10**7)


def dfs(v, p, depth, up, g, LOG):
    up[v][0] = p
    for i in range(1, LOG):
        up[v][i] = up[up[v][i - 1]][i - 1] if up[v][i - 1] != -1 else -1
    for to in g[v]:
        if to == p:
            continue
        depth[to] = depth[v] + 1
        dfs(to, v, depth, up, g, LOG)


def lca(a, b, depth, up, LOG):
    if depth[a] < depth[b]:
        a, b = b, a
    d = depth[a] - depth[b]
    for i in range(LOG):  # 深い方を、深さの差だけ上げる
        if d >> i & 1:
            a = up[a][i]
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):  # 祖先が分かれる直前まで一緒に上げる
        if up[a][i] != up[b][i]:
            a = up[a][i]
            b = up[b][i]
    return up[a][0]


def build_lca(g, root=0):
    n = len(g)
    LOG = max(1, n.bit_length())  # 2^LOG > n なので、深さの差（< n）を表せる
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n
    dfs(root, -1, depth, up, g, LOG)
    return depth, up, LOG


def main() -> None:
    n = 7
    g = [[] for _ in range(n)]
    for u, v in [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]:
        g[u].append(v)
        g[v].append(u)
    depth, up, LOG = build_lca(g)
    print(lca(3, 5, depth, up, LOG), lca(4, 6, depth, up, LOG))


if __name__ == "__main__":
    main()
