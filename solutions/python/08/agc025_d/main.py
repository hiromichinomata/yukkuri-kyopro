import sys


def coloring(d: int):
    """距離の 2 乗が d の 2 点を、必ず違う色（0/1）に塗る塗り方を返す"""
    t = 0
    while d % 4 == 0:  # d = 4^t × r（r は 4 で割り切れない）
        d //= 4
        t += 1
    if d % 2 == 1:
        # dx^2 + dy^2 が奇数 → (dx + dy) が奇数。市松模様で色が変わる
        return lambda x, y: ((x >> t) + (y >> t)) & 1
    # d ≡ 2 (mod 4) → dx, dy はともに奇数。x の偶奇で色が変わる
    return lambda x, y: (x >> t) & 1


def main() -> None:
    n, d1, d2 = map(int, sys.stdin.readline().split())
    c1, c2 = coloring(d1), coloring(d2)
    groups = [[] for _ in range(4)]
    for x in range(2 * n):
        for y in range(2 * n):
            groups[c1(x, y) * 2 + c2(x, y)].append((x, y))
    # 4N^2 個の点を 4 グループに分けたので、どれかは N^2 個以上ある（鳩の巣原理）
    best = max(groups, key=len)
    out = [f"{x} {y}" for x, y in best[: n * n]]
    print("\n".join(out))


if __name__ == "__main__":
    main()
