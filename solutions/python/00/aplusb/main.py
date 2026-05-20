import sys


def main() -> None:
    a, b = map(int, sys.stdin.read().split())
    print(a + b)


if __name__ == "__main__":
    main()
