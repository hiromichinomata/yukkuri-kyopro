import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    out = []
    prefix = 0  # A_1 + ... + A_k
    prefix_of_prefix = 0  # (A_1) + (A_1 + A_2) + ... + (A_1 + ... + A_k)
    mx = 0  # max(A_1, ..., A_k)
    for k, x in enumerate(a, start=1):
        prefix += x
        prefix_of_prefix += prefix
        mx = max(mx, x)
        # 操作後の和 = 累積和の累積和 + k × 最大値（愚直な操作と比べて確かめられる）
        out.append(prefix_of_prefix + k * mx)
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    main()
