def scc(g, n):
    order = []
    seen = [False] * n

    def dfs(v):
        seen[v] = True
        for to in g[v]:
            if not seen[to]:
                dfs(to)
        order.append(v)

    for i in range(n):
        if not seen[i]:
            dfs(i)

    rg = [[] for _ in range(n)]
    for v in range(n):
        for to in g[v]:
            rg[to].append(v)

    comp = [-1] * n
    cid = 0
    seen = [False] * n

    def rdfs(v):
        seen[v] = True
        comp[v] = cid
        for to in rg[v]:
            if not seen[to]:
                rdfs(to)

    for v in reversed(order):
        if not seen[v]:
            rdfs(v)
            cid += 1
    return comp, cid


def main() -> None:
    n = 5
    g = [[] for _ in range(n)]
    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)]
    for u, v in edges:
        g[u].append(v)
    comp, k = scc(g, n)
    print(k, comp)


if __name__ == "__main__":
    main()
