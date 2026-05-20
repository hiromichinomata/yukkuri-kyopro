import sys


def main() -> None:
    input = sys.stdin.readline
    n, q = map(int, input().split())
    for _ in range(q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        d = abs(a - b)
        print(min(d, n - d))


if __name__ == "__main__":
    main()
