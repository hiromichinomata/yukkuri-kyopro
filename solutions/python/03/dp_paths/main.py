def paths(h: int, w: int, blocked: list) -> int:
    dp = [[0] * w for _ in range(h)]
    if not blocked[0][0]:
        dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if blocked[i][j]:
                dp[i][j] = 0
                continue
            if i:
                dp[i][j] += dp[i - 1][j]
            if j:
                dp[i][j] += dp[i][j - 1]
    return dp[h - 1][w - 1]


def main() -> None:
    blocked = [[False] * 3 for _ in range(3)]
    blocked[1][1] = True
    print(paths(3, 3, blocked))


if __name__ == "__main__":
    main()
