import sys
from math import gcd


def first_in_range(a: int, m: int, lo: int, hi: int) -> int:
    """(a*x mod m) が lo 以上 hi 以下になる最小の x ≥ 0（0 ≤ lo ≤ hi < m）。なければ -1。
    ユークリッドの互除法と同じ形で (a, m) → (m mod a, a) と小さくしていくので O(log m)"""
    if lo == 0:
        return 0
    a %= m
    if a == 0:
        return -1
    x = (lo + a - 1) // a  # 折り返さずに届く最小の x
    if a * x <= hi:
        return x
    # a*x = m*y + (lo〜hi) となる最小の y を探す。⇔ (m*y mod a) が (-hi mod a)〜(-lo mod a) にある
    y = first_in_range(m % a, a, (-hi) % a, (-lo) % a)
    if y == -1:
        return -1
    return (m * y + lo + a - 1) // a


def solve(n: int, a: int, b: int):
    g = gcd(a, b)
    # 最長の区間では L-1 と R+1 が a の倍数: L = a*l + 1, R = a*r - 1。k = r - l とすると
    # a の倍数は k-1 個、b の倍数は「区間の左端から最初の b の倍数までのずれ t」が小さいほど多い。
    # 長さ k・ずれ t で作れる ⇔ (k-1) - floor((a*k - 1 + b - t) / b) ≤ n
    # ⇔ t ≤ a*k - 1 + b - b*(k-1-n)。t の最小は g なので、k の最大は次の式で求まる
    k = (b * (n + 2) - 1 - g) // (b - a)
    c = min(b, a * k - 1 + b - b * (k - 1 - n))  # この k で許される t の上限
    # t は「a*l の次の b の倍数までの距離」: (a*l mod b) が 0 なら t = b、そうでなければ b - (a*l mod b)
    if c >= b:
        l = 0  # どの l でもよい → 最小の 0
    else:
        l = first_in_range(a, b, b - c, b - 1)  # (a*l mod b) ≥ b - c となる最小の l
    return a * l + 1, a * (l + k) - 1


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, a, b = int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i])
        L, R = solve(n, a, b)
        out.append(f"{L} {R}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
