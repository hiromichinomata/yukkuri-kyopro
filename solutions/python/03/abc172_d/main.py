import sys


def main() -> None:
    n = int(sys.stdin.readline())
    # 主客転倒: K × f(K) の和 = 「d が約数になる K」すべてについての K の和を、d ごとに足したもの。
    # d の倍数 d, 2d, …, md（m = N // d）の和は d × m(m+1)/2
    ans = 0
    for d in range(1, n + 1):
        m = n // d
        ans += d * m * (m + 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
