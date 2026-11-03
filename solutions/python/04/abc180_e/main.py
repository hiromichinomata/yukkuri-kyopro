import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    p = [tuple(map(int, input().split())) for _ in range(n)]

    def cost(i, j):
        (a, b, c), (x, y, z) = p[i], p[j]
        return abs(x - a) + abs(y - b) + max(0, z - c)

    # この費用は三角不等式を満たすので、各都市をちょうど 1 回ずつ回る巡回でよい（巡回セールスマン）
    INF = 10**18
    dist = [[cost(i, j) for j in range(n)] for i in range(n)]
    # dp[mask][v]: 訪れた都市の集合 mask、いま v にいるときの最小費用
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1 << n):
        row = dp[mask]
        for v in range(n):
            cur = row[v]
            if cur == INF:
                continue
            for to in range(n):
                if mask >> to & 1:
                    continue
                nm = mask | 1 << to
                if cur + dist[v][to] < dp[nm][to]:
                    dp[nm][to] = cur + dist[v][to]
    full = (1 << n) - 1
    print(min(dp[full][v] + dist[v][0] for v in range(n)))


if __name__ == "__main__":
    main()
