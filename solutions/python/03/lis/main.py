def lis(a: list) -> int:
    n = len(a)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def main() -> None:
    print(lis([3, 1, 4, 2, 5]))


if __name__ == "__main__":
    main()
