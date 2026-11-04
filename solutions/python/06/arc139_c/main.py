import sys


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    # X と Y を入れ替えても条件は同じ形なので、N ≤ M にそろえて作り、最後に戻す
    swap = n > m
    if swap:
        n, m = m, n
    # 3X + Y は 4〜3N+M の 3N+M-3 通りしかないので、それが上限（N = M が偶数のときだけ 1 少ない）。
    # 3X + Y が 1 ずつ増えるように「右へ 1」「下へ 1・左へ 2」で進む階段状の道を作ると、
    # X + 3Y も重ならずに上限を達成できる
    pts = []
    for x in range(1, n + 1):
        if x == n:
            lo, hi = (n - 2 if n % 2 else n - 1), m  # 最後の行は右端まで
        elif x % 2 == 1:
            lo, hi = x - 2, x + 2
        else:
            lo, hi = x - 1, x + 1
        for y in range(max(1, lo), min(m, hi) + 1):
            pts.append((y, x) if swap else (x, y))
    out = [str(len(pts))] + [f"{x} {y}" for x, y in pts]
    print("\n".join(out))


if __name__ == "__main__":
    main()
