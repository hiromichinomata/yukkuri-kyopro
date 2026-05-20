import sys
from functools import lru_cache


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)

    @lru_cache(maxsize=None)
    def advantage(l: int, r: int) -> int:
        """区間 [l,r] で手番のプレイヤーが得する (自分の合計 - 相手の合計) の最大値。"""
        if l == r:
            return a[l]
        return max(a[l] - advantage(l + 1, r), a[r] - advantage(l, r - 1))

    # 先手（高橋）の合計 = (全体の和 + 先手有利度) / 2
    print((total + advantage(0, n - 1)) // 2)


if __name__ == "__main__":
    main()
