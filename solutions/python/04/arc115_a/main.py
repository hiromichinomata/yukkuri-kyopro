import sys


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    odd = 0  # 「1」の個数が奇数の人数
    for _ in range(n):
        if input().strip().count("1") % 2 == 1:
            odd += 1
    even = n - odd
    # 正解数の差の偶奇は、2 人の「1」の個数の偶奇の差で決まる。
    # 偶奇が違うペアは、どんな正解でも同点にならない
    print(odd * even)


if __name__ == "__main__":
    main()
