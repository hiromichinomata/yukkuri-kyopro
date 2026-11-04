import sys
from itertools import combinations


def construct(n: int):
    """1..n を和の等しい 2 グループに分ける。不可能なら None。
    必要条件: 総和 n(n+1)/2 が偶数 ⇔ n % 4 が 0 か 3。これは十分でもある（下の構成）"""
    if n % 4 in (1, 2):
        return None
    a, b = [], []
    start = 1
    if n % 4 == 3:
        a += [1, 2]  # 1 + 2 = 3 で釣り合わせてから、残り 4..n を 4 個ずつ処理
        b += [3]
        start = 4
    # 連続する 4 個 k, k+1, k+2, k+3 は k + (k+3) = (k+1) + (k+2) で分けられる
    for k in range(start, n + 1, 4):
        a += [k, k + 3]
        b += [k + 1, k + 2]
    return a, b


def exists_by_brute(n: int) -> bool:
    total = n * (n + 1) // 2
    if total % 2:
        return False
    nums = range(1, n + 1)
    return any(sum(c) == total // 2 for r in range(n + 1) for c in combinations(nums, r))


def main() -> None:
    # 構成の検証: 小さい n で全探索の「可能 / 不可能」と一致し、構成が正しいか
    for n in range(1, 16):
        res = construct(n)
        assert (res is not None) == exists_by_brute(n), n
        if res:
            a, b = res
            assert sorted(a + b) == list(range(1, n + 1)) and sum(a) == sum(b), n
    n = int(sys.stdin.readline())
    res = construct(n)
    if res is None:
        print(-1)
    else:
        a, b = res
        print(*sorted(a))
        print(*sorted(b))


if __name__ == "__main__":
    main()
