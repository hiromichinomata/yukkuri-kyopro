import sys

MOD = 10**9 + 7


def count_digit_sum_multiple(k: str, d: int) -> int:
    """1 以上 K 以下で、各桁の和が D の倍数になる整数の個数（mod 1e9+7）"""
    # dp[tight][r]: 上の桁から決めてきて、桁和 mod D が r の個数
    #   tight=1: ここまで K と完全に一致（次の桁は K の桁以下しか置けない）
    #   tight=0: すでに K より小さい（次の桁は 0〜9 を自由に置ける）
    dp = [[0] * d for _ in range(2)]
    dp[1][0] = 1
    for ch in k:
        x = int(ch)
        ndp = [[0] * d for _ in range(2)]
        for tight in range(2):
            for r in range(d):
                cur = dp[tight][r]
                if cur == 0:
                    continue
                limit = x if tight else 9
                for digit in range(limit + 1):
                    nt = 1 if (tight and digit == limit) else 0
                    nr = (r + digit) % d
                    ndp[nt][nr] = (ndp[nt][nr] + cur) % MOD
        dp = ndp
    # 0 も「桁和 0」で数えてしまっているので 1 引く
    return (dp[0][0] + dp[1][0] - 1) % MOD


def main() -> None:
    input = sys.stdin.readline
    k = input().strip()
    d = int(input())
    print(count_digit_sum_multiple(k, d))


if __name__ == "__main__":
    main()
