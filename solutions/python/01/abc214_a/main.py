import sys


def main() -> None:
    n = int(sys.stdin.readline())
    if n <= 125:
        print(4)
    elif n <= 211:
        print(6)
    else:
        print(8)


if __name__ == "__main__":
    main()
