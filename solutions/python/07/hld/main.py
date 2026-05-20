import sys

sys.setrecursionlimit(10**7)


def main() -> None:
    n = 7
    g = [[] for _ in range(n)]
    for u, v in [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]:
        g[u].append(v)
        g[v].append(u)

    parent = [-1] * n
    depth = [0] * n
    size = [0] * n
    head = [-1] * n
    pos = [0] * n
    cur = [0]

    def dfs_size(v, p):
        size[v] = 1
        parent[v] = p
        for to in g[v]:
            if to == p:
                continue
            depth[to] = depth[v] + 1
            dfs_size(to, v)
            size[v] += size[to]

    def dfs_hld(v, p, h):
        head[v] = h
        pos[v] = cur[0]
        cur[0] += 1
        heavy = -1
        for to in g[v]:
            if to == p:
                continue
            if heavy == -1 or size[to] > size[heavy]:
                heavy = to
        if heavy != -1:
            dfs_hld(heavy, v, h)
        for to in g[v]:
            if to != p and to != heavy:
                dfs_hld(to, v, to)

    dfs_size(0, -1)
    dfs_hld(0, -1, 0)

    def lca(a, b):
        while head[a] != head[b]:
            if depth[head[a]] > depth[head[b]]:
                a = parent[head[a]]
            else:
                b = parent[head[b]]
        return a if depth[a] < depth[b] else b

    print(lca(3, 5), lca(4, 6))
    print(head, pos)


if __name__ == "__main__":
    main()
