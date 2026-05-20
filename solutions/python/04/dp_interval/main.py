def merge_stones(a):
    n = len(a)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            dp[l][r] = min(dp[l][k] + dp[k + 1][r] for k in range(l, r)) + sum(a[l : r + 1])
    return dp[0][n - 1]


def main() -> None:
    print(merge_stones([4, 1, 2, 3]))


if __name__ == "__main__":
    main()
