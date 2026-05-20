import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    jobs = []
    for _ in range(n):
        d, p = map(int, input().split())
        jobs.append((d, p))
    jobs.sort()
    maxd = max(d for d, _ in jobs)
    dp = [0] * (maxd + 2)
    for d, p in jobs:
        for i in range(maxd, d - 1, -1):
            dp[i] = max(dp[i], dp[d - 1] + p)
    print(max(dp))


if __name__ == "__main__":
    main()
