import sys

sys.setrecursionlimit(10**7)


def dfs(v, parent, g, dp):
    dp[v] = 1
    for to in g[v]:
        if to == parent:
            continue
        dfs(to, v, g, dp)
        dp[v] += dp[to]


def main() -> None:
    g = [[1, 2], [0, 3], [0], [1]]
    dp = [0] * 4
    dfs(0, -1, g, dp)
    print(dp)


if __name__ == "__main__":
    main()
