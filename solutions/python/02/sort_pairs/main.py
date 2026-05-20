import sys


def main() -> None:
    pairs = [(1, 3), (2, 1), (4, 2)]
    pairs.sort(key=lambda x: x[1])
    print(pairs)


if __name__ == "__main__":
    main()
