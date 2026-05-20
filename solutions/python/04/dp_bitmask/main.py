def tsp(dist, n):
    INF = 10**18
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1 << n):
        for i in range(n):
            if dp[mask][i] == INF:
                continue
            for j in range(n):
                if mask >> j & 1:
                    continue
                nmask = mask | (1 << j)
                dp[nmask][j] = min(dp[nmask][j], dp[mask][i] + dist[i][j])
    full = (1 << n) - 1
    return min(dp[full][i] for i in range(n))


def main() -> None:
    dist = [
        [0, 2, 9],
        [2, 0, 6],
        [9, 6, 0],
    ]
    print(tsp(dist, 3))


if __name__ == "__main__":
    main()
