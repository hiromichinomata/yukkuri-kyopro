import sys


def sum_of_all_subarray_sums(a: list) -> int:
    """すべての連続部分列の和の総和。a[i] が何個の区間に含まれるかで数える"""
    n = len(a)
    total = 0
    for i, x in enumerate(a):
        left = i + 1  # 区間の左端の選び方: 0..i
        right = n - i  # 区間の右端の選び方: i..n-1
        total += x * left * right
    return total


def sum_of_pair_diffs(a: list) -> int:
    """i < j のすべてのペアの |a_i - a_j| の総和。ソートして寄与で数える"""
    b = sorted(a)
    total = 0
    for i, x in enumerate(b):
        # x は自分より左の i 個に対して「大きい方」として +x、
        # 右の n-1-i 個に対して「小さい方」として -x される
        total += x * i - x * (len(b) - 1 - i)
    return total


def expected_records(n: int) -> float:
    """1..n のランダムな順列で「それまでの最大値を更新する位置」の個数の期待値。
    位置 i（1-indexed）が更新になる確率は 1/i なので、期待値の線形性で和を取る"""
    return sum(1 / i for i in range(1, n + 1))


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    print(sum_of_all_subarray_sums(a))
    print(sum_of_pair_diffs(a))
    print(f"{expected_records(n):.6f}")


if __name__ == "__main__":
    main()
