import sys

sys.setrecursionlimit(10**7)  # 問題に応じて調整


def dfs(v: int, g: list, seen: list) -> None:
    seen[v] = True
    for to in g[v]:
        if not seen[to]:
            dfs(to, g, seen)


def main() -> None:
    # 0 — 1, 2 の木で DFS（例）。たどり着いた頂点の数を出力する
    g = [[1, 2], [], []]
    seen = [False] * 3
    dfs(0, g, seen)
    print(sum(seen))


if __name__ == "__main__":
    main()
