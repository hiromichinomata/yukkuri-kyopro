import sys


def main() -> None:
    s = sys.stdin.readline().strip()
    print(len(s.replace("0", "")))


if __name__ == "__main__":
    main()
