import sys


def main() -> None:
    input = sys.stdin.readline
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    # 全部の技を 1 回ずつ使うのが最大のダメージ
    print("Yes" if sum(a) >= h else "No")


if __name__ == "__main__":
    main()
