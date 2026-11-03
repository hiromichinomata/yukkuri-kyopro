import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    d = [int(input()) for _ in range(n)]
    # 直径が真に小さいものしか上に積めない → 使えるのは「異なる直径」の種類数だけ
    print(len(set(d)))


if __name__ == "__main__":
    main()
