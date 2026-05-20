import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    xs = [int(input()) for _ in range(n)]
    print(sum(xs))


if __name__ == "__main__":
    main()
