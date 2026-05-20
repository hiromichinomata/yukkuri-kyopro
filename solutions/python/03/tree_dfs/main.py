import sys

sys.setrecursionlimit(10**7)


def dfs(v: int, parent: int, g: list, depth: list) -> None:
    depth[v] = depth[parent] + 1 if parent != -1 else 0
    for to in g[v]:
        if to == parent:
            continue
        dfs(to, v, g, depth)


def main() -> None:
    g = [[1, 2], [0, 3], [0], [1]]
    depth = [0] * 4
    dfs(0, -1, g, depth)
    print(depth)


if __name__ == "__main__":
    main()
