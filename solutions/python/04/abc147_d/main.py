import sys

MOD = 10**9 + 7


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for b in range(60):  # ビットごとに寄与を数える（主客転倒）
        ones = sum(x >> b & 1 for x in a)
        # b ビット目が 1 になる組 = 「1 の数」×「0 の数」。それぞれ 2^b ずつ寄与する
        ans = (ans + ones * (n - ones) % MOD * pow(2, b, MOD)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
