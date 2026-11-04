import sys

"""
ARC104 A - Plus Minus
X + Y = A、X - Y = B を満たす整数 X, Y を求める。
2 式を足すと 2X = A + B、引くと 2Y = A - B。
"""


def main() -> None:
    a, b = map(int, sys.stdin.readline().split())
    print((a + b) // 2, (a - b) // 2)


if __name__ == "__main__":
    main()
