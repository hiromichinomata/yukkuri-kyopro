import sys
from math import gcd


def floor_sum(n: int, m: int, a: int, b: int) -> int:
    """sum_{i=0}^{n-1} floor((a*i + b) / m)（AtCoder Library と同じ計算）"""
    ans = 0
    while True:
        if a >= m:
            ans += (n - 1) * n // 2 * (a // m)
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
        y_max = a * n + b
        if y_max < m:
            return ans
        n, b, m, a = y_max // m, y_max % m, a, m


def solve(n: int, a: int, b: int):
    g = gcd(a, b)
    # 最長の区間では L-1 と R+1 が a の倍数: L = a*l + 1, R = a*r - 1。k = r - l とすると
    # a の倍数は k-1 個、b の倍数は「区間の左端から最初の b の倍数までのずれ t」が小さいほど多い。
    # t の最小は g なので、長さ k が作れる ⇔ (k-1) - floor((a*k - 1 + b - g) / b) ≤ n。左辺は k について単調
    def f(k, t):
        return (k - 1) - (a * k - 1 + b - t) // b

    lo, hi = 1, 1
    while f(hi, g) <= n:
        hi *= 2
    while hi - lo > 1:  # f(lo) ≤ n < f(hi)
        mid = (lo + hi) // 2
        if f(mid, g) <= n:
            lo = mid
        else:
            hi = mid
    k = lo
    # この k で条件を満たす t の上限 c（t ≤ c なら OK）
    tl, th = g, b + 1  # f(k, tl) ≤ n、th は不可（または範囲外）
    while th - tl > 1:
        mid = (tl + th) // 2
        if f(k, mid) <= n:
            tl = mid
        else:
            th = mid
    c = tl
    # t は「a*l の次の b の倍数までの距離」: (a*l mod b) が 0 なら t = b、そうでなければ b - (a*l mod b)
    if c >= b:
        l = 0  # どの l でもよい → 最小の 0
    else:
        # (a*x mod b) ≥ b - c となる最小の x ≥ 1 を、個数の数え上げ（floor_sum）と二分探索で求める
        def count(x):  # 1〜x のうち条件を満たす個数
            return floor_sum(x + 1, b, a, c) - floor_sum(x + 1, b, a, 0)

        lo2, hi2 = 0, b  # count(lo2) = 0, count(hi2) ≥ 1（周期 b の中に必ずある）
        while hi2 - lo2 > 1:
            mid = (lo2 + hi2) // 2
            if count(mid) >= 1:
                hi2 = mid
            else:
                lo2 = mid
        l = hi2
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
