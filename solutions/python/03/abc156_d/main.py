import sys

MOD = 10**9 + 7


def comb(n: int, r: int) -> int:
    """n が大きく r が小さいとき: n(n-1)…(n-r+1) / r! を mod で計算"""
    num = den = 1
    for i in range(r):
        num = num * (n - i) % MOD
        den = den * (i + 1) % MOD
    return num * pow(den, MOD - 2, MOD) % MOD


def main() -> None:
    n, a, b = map(int, sys.stdin.readline().split())
    # 1 本以上の選び方 2^n - 1 から、a 本・b 本の選び方を引く
    ans = (pow(2, n, MOD) - 1 - comb(n, a) - comb(n, b)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
