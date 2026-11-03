import sys


def main() -> None:
    a, b = map(int, sys.stdin.readline().split())
    s = str(a) * b  # 数字 a を b 個
    t = str(b) * a  # 数字 b を a 個
    print(min(s, t))  # 文字列の min は辞書順で比べる


if __name__ == "__main__":
    main()
