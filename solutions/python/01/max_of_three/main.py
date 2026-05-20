import sys


def main() -> None:
    a, b, c = map(int, sys.stdin.readline().split())
    print(max(a, b, c))


if __name__ == "__main__":
    main()
