import sys


def main() -> None:
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    cum = [0] * (n + 1)
    for i in range(1, n + 1):
        cum[i] = cum[i - 1] + a[i]
    out = []
    for _ in range(q):
        l, r = map(int, input().split())
        out.append(str(cum[r] - cum[l - 1]))
    print("\n".join(out))


if __name__ == "__main__":
    main()
