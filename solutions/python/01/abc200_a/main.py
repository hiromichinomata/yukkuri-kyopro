import sys


def main() -> None:
    n = int(sys.stdin.readline())
    print((n + 99) // 100)  # 100 で割って切り上げ（1〜100 年が 1 世紀）


if __name__ == "__main__":
    main()
