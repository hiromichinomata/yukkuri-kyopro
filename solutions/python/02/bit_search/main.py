import sys


def main() -> None:
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for mask in range(1 << n):  # 0 〜 2^n - 1 の全部分集合
        s = 0
        for i in range(n):
            if mask >> i & 1:  # i ビット目が 1 なら a[i] を選ぶ
                s += a[i]
        if s == k:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
