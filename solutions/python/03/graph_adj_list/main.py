def main() -> None:
    n = 5
    g = [[] for _ in range(n)]
    for u, v in [(0, 1), (0, 2), (1, 3), (2, 4)]:
        g[u].append(v)
        g[v].append(u)
    print(g)


if __name__ == "__main__":
    main()
