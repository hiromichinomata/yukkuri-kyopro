import sys

MOD = 10**9 + 7


def main() -> None:
    input = sys.stdin.readline
    k = input().strip()
    d = int(input())
    # dp[tight][r]: 上の桁から決めて、桁和を D で割った余りが r の数の個数
    dp = [[0] * d for _ in range(2)]
    dp[1][0] = 1
    for ch in k:
        lim = int(ch)
        ndp = [[0] * d for _ in range(2)]
        for r in range(d):
            free = dp[0][r]
            if free:
                for x in range(10):  # すでに K より小さい → 0〜9 を自由に置ける
                    nr = (r + x) % d
                    ndp[0][nr] = (ndp[0][nr] + free) % MOD
            tight = dp[1][r]
            if tight:
                for x in range(lim + 1):
                    nr = (r + x) % d
                    nt = 1 if x == lim else 0
                    ndp[nt][nr] = (ndp[nt][nr] + tight) % MOD
        dp = ndp
    # 0〜K のうち桁和が D の倍数のもの。0 自身を除く
    print((dp[0][0] + dp[1][0] - 1) % MOD)


if __name__ == "__main__":
    main()
