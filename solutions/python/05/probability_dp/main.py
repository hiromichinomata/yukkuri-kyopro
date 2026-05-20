def prob_reach(n: int, max_face: int = 6) -> float:
    dp = [0.0] * (n + 1)
    dp[0] = 1.0
    for i in range(n):
        for f in range(1, max_face + 1):
            if i + f <= n:
                dp[i + f] += dp[i] / max_face
    return dp[n]


def main() -> None:
    print(prob_reach(6, 6))


if __name__ == "__main__":
    main()
