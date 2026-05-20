import sys


def main() -> None:
    a, b = map(int, sys.stdin.readline().split())
    p = a * b
    print("Yes" if 1 <= p <= 9 else "No")


if __name__ == "__main__":
    main()
