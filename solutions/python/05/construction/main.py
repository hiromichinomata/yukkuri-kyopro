import sys
from itertools import permutations


def is_valid(p: list) -> bool:
    """隣り合う差の絶対値がすべて異なるか"""
    diffs = [abs(p[i + 1] - p[i]) for i in range(len(p) - 1)]
    return len(set(diffs)) == len(diffs)


def construct(n: int) -> list:
    """1, n, 2, n-1, 3, ... と左右から交互に取ると、差が n-1, n-2, ..., 1 になる"""
    res = []
    lo, hi = 1, n
    while lo <= hi:
        res.append(lo)
        if lo != hi:
            res.append(hi)
        lo += 1
        hi -= 1
    return res


def experiment(max_n: int) -> None:
    """小さい n で全探索し、条件を満たす順列の例と個数を見る（考察用）"""
    for n in range(1, max_n + 1):
        ok = [p for p in permutations(range(1, n + 1)) if is_valid(list(p))]
        print(f"n={n}: {len(ok)} 個, 例 {list(ok[0])}", file=sys.stderr)


def main() -> None:
    n = int(sys.stdin.readline())
    # experiment(6)  # 考察中だけ有効にする（提出時はコメントアウト）
    p = construct(n)
    assert is_valid(p)
    print(*p)


if __name__ == "__main__":
    main()
