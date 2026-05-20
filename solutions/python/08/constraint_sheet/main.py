def analyze_constraints(n, q, vmax, graph=False):
    hints = []
    if n <= 20:
        hints.append("bitmask / meet-in-the-middle")
    if n <= 2000 and q <= 2000:
        hints.append("O(N^2) DP or Floyd")
    if graph:
        hints.append("tree? -> LCA/HLD; general -> flow/SCC/2-SAT")
    if q >= 10**5:
        hints.append("log or sqrt decomposition, segtree/Fenwick")
    if vmax <= 10**6:
        hints.append("coordinate compression")
    return hints


def main() -> None:
    print(analyze_constraints(18, 0, 10**9))
    print(analyze_constraints(200000, 200000, 10**9, graph=True))


if __name__ == "__main__":
    main()
