import sys


def main() -> None:
    input = sys.stdin.readline
    s = input().strip()
    k = int(input())
    # dp[tight][c]: 上の桁から決めて、0 でない桁を c 個使った数の個数
    # tight = 1 は「ここまで N と同じ」、0 は「すでに N より小さい」
    dp = [[0] * (k + 2) for _ in range(2)]
    dp[1][0] = 1
    for ch in s:
        d = int(ch)
        ndp = [[0] * (k + 2) for _ in range(2)]
        for tight in range(2):
            for c in range(k + 1):
                if dp[tight][c] == 0:
                    continue
                limit = d if tight else 9
                for x in range(limit + 1):
                    nt = 1 if tight and x == limit else 0
                    nc = min(c + (x != 0), k + 1)  # K を超えたら k+1 にまとめる
                    ndp[nt][nc] += dp[tight][c]
        dp = ndp
    print(dp[0][k] + dp[1][k])  # 0 は 0 でない桁が 0 個なので K ≥ 1 では数えられない


if __name__ == "__main__":
    main()
