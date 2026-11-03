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


# リテラルの番号: 2*i が「x_i が真」、2*i+1 が「x_i が偽」。l ^ 1 で否定になる
def add_clause(implications, a, b):
    # 節 (a ∨ b) は「¬a なら b」「¬b なら a」の 2 本の含意
    implications.append((a ^ 1, b))
    implications.append((b ^ 1, a))

def sat2_solvable(implications, n_vars):
    n = 2 * n_vars
    g = [[] for _ in range(n)]
    for a, b in implications:
        g[a].append(b)
    comp, _ = scc(g, n)
    for i in range(n_vars):
        if comp[2 * i] == comp[2 * i + 1]:  # x と ¬x が同じ成分なら矛盾
            return False
    return True


def main() -> None:
    # (x0 ∨ x1) ∧ (¬x0 ∨ x1) ∧ (¬x1 ∨ x0) → x0 = x1 = 真 で充足可能
    imp = []
    add_clause(imp, 0, 2)
    add_clause(imp, 1, 2)
    add_clause(imp, 3, 0)
    print("Yes" if sat2_solvable(imp, 2) else "No")
    # さらに (¬x0 ∨ ¬x1) を足すと充足不能
    add_clause(imp, 1, 3)
    print("Yes" if sat2_solvable(imp, 2) else "No")


if __name__ == "__main__":
    main()
