import sys


def main() -> None:
    s = sys.stdin.readline().rstrip("\n")
    print("AC" if s == "Hello,World!" else "WA")  # 大文字・記号まで完全一致


if __name__ == "__main__":
    main()
