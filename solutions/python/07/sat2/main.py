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
    return comp


def sat2_solvable(implications, n_vars):
    n = 2 * n_vars
    g = [[] for _ in range(n)]
    for a, b in implications:
        g[a].append(b)
    comp = scc(g, n)
    for i in range(n_vars):
        if comp[2 * i] == comp[2 * i + 1]:
            return False
    return True


def main() -> None:
    n_vars = 2
    implications = [(1, 2), (3, 2)]
    print(sat2_solvable(implications, n_vars))


if __name__ == "__main__":
    main()
