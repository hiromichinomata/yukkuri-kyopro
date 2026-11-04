import sys


def main() -> None:
    a = sorted(map(int, sys.stdin.readline().split()))  # 並べ替えてよいので、小さい順にして調べる
    print("Yes" if a[2] - a[1] == a[1] - a[0] else "No")


if __name__ == "__main__":
    main()
