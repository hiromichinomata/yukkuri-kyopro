import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    # 部分和 s と「残り」total - s は 1 対 1 に対応する（対称性）。
    # 空集合を含めた 2^N 個の部分和の中央で、total / 2 以上の最小の部分和が答え。
    bits = 1  # i ビット目が 1 ⇔ 部分和 i が作れる（Python の int を bitset として使う）
    for x in a:
        bits |= bits << x
    bits >>= (total + 1) // 2  # total / 2 以上の部分だけ残す
    low = bits & -bits  # 一番下の 1 のビット
    print((total + 1) // 2 + low.bit_length() - 1)


if __name__ == "__main__":
    main()
