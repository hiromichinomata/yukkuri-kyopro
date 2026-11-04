import sys


def main() -> None:
    input = sys.stdin.readline
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    print(sum(1 for x in h if x >= k))


if __name__ == "__main__":
    main()
