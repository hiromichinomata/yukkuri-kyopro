def knapsack(weights: list, values: list, cap: int) -> int:
    dp = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]


def main() -> None:
    weights = [2, 3, 4]
    values = [3, 4, 5]
    print(knapsack(weights, values, 5))


if __name__ == "__main__":
    main()
