import sys

sys.setrecursionlimit(10**7)


def dfs_size(v, p, g, size, parent, depth):
    size[v] = 1
    parent[v] = p
    for to in g[v]:
        if to == p:
            continue
        depth[to] = depth[v] + 1
        dfs_size(to, v, g, size, parent, depth)
        size[v] += size[to]


def dfs_hld(v, p, h, g, size, head, pos, cur):
    """h: v が属する重い鎖の先頭。pos: 鎖が連続するように振った番号"""
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
        dfs_hld(heavy, v, h, g, size, head, pos, cur)  # 重い子は同じ鎖
    for to in g[v]:
        if to != p and to != heavy:
            dfs_hld(to, v, to, g, size, head, pos, cur)  # 軽い子は新しい鎖の先頭


def build_hld(g, root=0):
    n = len(g)
    size, parent, depth = [0] * n, [-1] * n, [0] * n
    head, pos = [0] * n, [0] * n
    dfs_size(root, -1, g, size, parent, depth)
    dfs_hld(root, -1, root, g, size, head, pos, [0])
    return parent, depth, head, pos


def hld_lca(a, b, parent, depth, head):
    while head[a] != head[b]:  # 鎖の先頭が深い方を、鎖ごと飛ばして上げる
        if depth[head[a]] > depth[head[b]]:
            a = parent[head[a]]
        else:
            b = parent[head[b]]
    return a if depth[a] < depth[b] else b


def main() -> None:
    n = 7
    g = [[] for _ in range(n)]
    for u, v in [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]:
        g[u].append(v)
        g[v].append(u)
    parent, depth, head, pos = build_hld(g)
    print(hld_lca(3, 5, parent, depth, head), hld_lca(4, 6, parent, depth, head))
    print(*head)
    print(*pos)


if __name__ == "__main__":
    main()
