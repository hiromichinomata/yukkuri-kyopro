import sys

"""
AGC004 A - Divide a Cuboid
A×B×C の直方体を、赤と青それぞれが直方体になるよう 2 つに切り分け、個数の差を最小化する。
どれかの辺が偶数なら半分に切れるので 0。全部奇数なら、ある辺を (k, k+1) に分けると
差は残り 2 辺の積になるので、その最小値が答え。
"""


def main() -> None:
    a, b, c = map(int, sys.stdin.readline().split())
    if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
        print(0)
    else:
        print(min(a * b, b * c, c * a))


if __name__ == "__main__":
    main()
