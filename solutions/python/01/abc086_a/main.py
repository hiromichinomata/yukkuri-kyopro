import sys


def main() -> None:
    a, b = map(int, sys.stdin.readline().split())
    if a * b % 2 == 0:  # 2 で割った余りが 0 なら偶数
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    main()
