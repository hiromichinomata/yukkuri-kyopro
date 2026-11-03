import sys

MOD = 10**9 + 7


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    broken = [False] * (n + 1)
    for _ in range(m):
        broken[int(input())] = True

    dp = [0] * (n + 1)  # dp[i]: i 段目にたどり着く方法の数
    dp[0] = 1
    for i in range(1, n + 1):
        if broken[i]:
            continue  # 壊れた段には乗れない → 0 のまま
        dp[i] = dp[i - 1]
        if i >= 2:
            dp[i] += dp[i - 2]
        dp[i] %= MOD
    print(dp[n])


if __name__ == "__main__":
    main()
