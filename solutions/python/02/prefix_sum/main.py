import sys


def main() -> None:
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))  # 1-indexed にする
    # cum[i] = a[1] + ... + a[i]
    cum = [0] * (n + 1)
    for i in range(1, n + 1):
        cum[i] = cum[i - 1] + a[i]

    for _ in range(q):
        l, r = map(int, input().split())
        print(cum[r] - cum[l - 1])  # 区間 [l, r] の和


if __name__ == "__main__":
    main()
