import sys
from collections import deque


def can_by_condition(s: str) -> bool:
    """考察で得た条件: 裏（'1'）の枚数が偶数なら全部表にできる"""
    return s.count("1") % 2 == 0


def can_by_bfs(s: str) -> bool:
    """小さい N 用の全探索: 隣り合う 2 枚を同時に裏返す操作で全部 '0' に到達できるか"""
    n = len(s)
    start, goal = int(s, 2), 0
    seen = {start}
    q = deque([start])
    while q:
        v = q.popleft()
        if v == goal:
            return True
        for i in range(n - 1):
            nv = v ^ (0b11 << i)  # 隣り合う 2 ビットを反転
            if nv not in seen:
                seen.add(nv)
                q.append(nv)
    return False


def main() -> None:
    # 必要十分性の確認: 長さ 1〜10 のすべての並びで、条件と全探索が一致するか
    for n in range(1, 11):
        for mask in range(1 << n):
            s = format(mask, f"0{n}b")
            assert can_by_condition(s) == can_by_bfs(s), s
    print("condition == bfs for all n <= 10")
    s = sys.stdin.readline().strip()
    print("Yes" if can_by_condition(s) else "No")


if __name__ == "__main__":
    main()
