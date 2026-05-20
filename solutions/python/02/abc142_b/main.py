import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = sorted(map(int, input().split()))
    k = 2
    total = 0
    for i, price in enumerate(a):
        remaining = n - i
        if remaining % k == 0:
            total += price // 2
        else:
            total += price
    print(total)


if __name__ == "__main__":
    main()
