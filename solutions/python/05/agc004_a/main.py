import sys

"""
AGC004 A: 喜びの会場
中間の部屋の値を xor する典型（詳細は AtCoder の問題文を参照）。
"""

def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        ans ^= a[i]
    print(ans)


if __name__ == "__main__":
    main()
