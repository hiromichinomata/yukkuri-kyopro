"""本文で解説した ARC / AGC の解答を、小さいランダム入力で愚直解と比べるテスト。"""

import io
import itertools
import random
import sys

from conftest import load

R = random.Random(20261104)


def run(rel: str, data: str) -> str:
    mod = load(rel)
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(data), io.StringIO()
    try:
        mod.main()
        return sys.stdout.getvalue()
    finally:
        sys.stdin, sys.stdout = old_in, old_out


def test_arc115_a():
    for _ in range(100):
        n, m = R.randint(2, 6), R.randint(1, 4)
        s = ["".join(R.choice("01") for _ in range(m)) for _ in range(n)]
        exp = 0
        for i, j in itertools.combinations(range(n), 2):
            can_tie = any(
                sum(c == k for c, k in zip(s[i], key)) == sum(c == k for c, k in zip(s[j], key))
                for key in itertools.product("01", repeat=m)
            )
            exp += not can_tie
        assert run("04/arc115_a", f"{n} {m}\n" + "\n".join(s) + "\n").split() == [str(exp)]


def test_arc120_a():
    for _ in range(100):
        a = [R.randint(1, 20) for _ in range(R.randint(1, 8))]
        exp = []
        for k in range(1, len(a) + 1):
            b = a[:k]
            for i in range(k):
                b[i] += max(b)
            exp.append(str(sum(b)))
        assert run("04/arc120_a", f"{len(a)}\n{' '.join(map(str, a))}\n").split() == exp


def test_arc146_b():
    def brute_cost(a, t):
        x = a
        while x & t != t:
            x += 1
        return x - a

    for _ in range(100):
        n = R.randint(1, 5)
        k = R.randint(1, n)
        m = R.randint(0, 30)
        a = [R.randint(0, 31) for _ in range(n)]
        exp = max(t for t in range(128) if sum(sorted(brute_cost(x, t) for x in a)[:k]) <= m)
        assert run("05/arc146_b", f"{n} {m} {k}\n{' '.join(map(str, a))}\n").split() == [str(exp)]


def test_arc170_b():
    for _ in range(100):
        n = R.randint(3, 30)
        a = [R.randint(1, 10) for _ in range(n)]
        exp = 0
        for l in range(n):
            for r in range(l, n):
                exp += any(a[j] - a[i] == a[k] - a[j] for i, j, k in itertools.combinations(range(l, r + 1), 3))
        assert run("05/arc170_b", f"{n}\n{' '.join(map(str, a))}\n").split() == [str(exp)]


def test_agc021_a():
    best = 0
    for n in range(1, 3000):
        best = max(best, sum(map(int, str(n))))
        assert run("06/agc021_a", f"{n}\n").split() == [str(best)]


def test_agc023_a():
    for _ in range(200):
        a = [R.randint(-3, 3) for _ in range(R.randint(1, 12))]
        exp = sum(1 for l in range(len(a)) for r in range(l, len(a)) if sum(a[l : r + 1]) == 0)
        assert run("06/agc023_a", f"{len(a)}\n{' '.join(map(str, a))}\n").split() == [str(exp)]


def test_agc020_c():
    for _ in range(200):
        a = [R.randint(1, 20) for _ in range(R.randint(1, 9))]
        sums = sorted(sum(c) for k in range(1, len(a) + 1) for c in itertools.combinations(a, k))
        exp = sums[2 ** (len(a) - 1) - 1]
        assert run("07/agc020_c", f"{len(a)}\n{' '.join(map(str, a))}\n").split() == [str(exp)]


def test_agc022_c():
    V = 6

    def can(a, b, ks):
        cur = {a}
        for k in sorted(ks, reverse=True):  # 各 k は 1 回ずつ、大きい順に使えば十分
            cur |= {v % k for v in cur}
        return b in cur

    for _ in range(60):
        n = R.randint(1, 3)
        a = [R.randint(0, V) for _ in range(n)]
        b = [R.randint(0, V) for _ in range(n)]
        exp = -1
        for mask in range(1 << V):
            ks = [k for k in range(1, V + 1) if mask >> (k - 1) & 1]
            if all(can(x, y, ks) for x, y in zip(a, b)):
                c = sum(1 << k for k in ks)
                exp = c if exp == -1 else min(exp, c)
        data = f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}\n"
        assert run("07/agc022_c", data).split() == [str(exp)]


def test_agc025_d():
    for _ in range(60):
        n = R.randint(1, 6)
        d1, d2 = R.randint(1, 60), R.randint(1, 60)
        out = run("08/agc025_d", f"{n} {d1} {d2}\n").split()
        pts = [(int(out[i]), int(out[i + 1])) for i in range(0, len(out), 2)]
        assert len(pts) == n * n == len(set(pts))
        assert all(0 <= x < 2 * n and 0 <= y < 2 * n for x, y in pts)
        for (x1, y1), (x2, y2) in itertools.combinations(pts, 2):
            d = (x1 - x2) ** 2 + (y1 - y2) ** 2
            assert d != d1 and d != d2


# ---------- Part 1〜3 の推奨問題（考察で式に言い換えたもの） ----------
def test_abc134_c():
    for _ in range(200):
        a = [R.randint(1, 5) for _ in range(R.randint(2, 8))]
        exp = [str(max(a[:i] + a[i + 1 :])) for i in range(len(a))]
        assert run("02/abc134_c", f"{len(a)}\n" + "\n".join(map(str, a)) + "\n").split() == exp


def test_abc213_c():
    for _ in range(200):
        h, w = R.randint(1, 6), R.randint(1, 6)
        cells = R.sample([(i, j) for i in range(1, h + 1) for j in range(1, w + 1)], R.randint(1, min(5, h * w)))
        rows = [i for i in range(1, h + 1) if any(a == i for a, _ in cells)]
        cols = [j for j in range(1, w + 1) if any(b == j for _, b in cells)]
        exp = []
        for a, b in cells:  # 空の行・列を消した後の位置
            exp += [str(rows.index(a) + 1), str(cols.index(b) + 1)]
        data = f"{h} {w} {len(cells)}\n" + "".join(f"{a} {b}\n" for a, b in cells)
        assert run("03/abc213_c", data).split() == exp


def test_abc214_d():
    for _ in range(200):
        n = R.randint(2, 8)
        edges = [(i + 1, R.randint(1, i), R.randint(1, 9)) for i in range(1, n)]
        g = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        def path_max(s, t):
            stack = [(s, 0, 0)]
            while stack:
                v, p, mx = stack.pop()
                if v == t:
                    return mx
                stack += [(to, v, max(mx, w)) for to, w in g[v] if to != p]

        exp = sum(path_max(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1))
        data = f"{n}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in edges)
        assert run("03/abc214_d", data).split() == [str(exp)]


def test_abc172_d():
    for n in list(range(1, 60)) + [997, 1000]:
        exp = sum(k * sum(1 for d in range(1, k + 1) if k % d == 0) for k in range(1, n + 1))
        assert run("03/abc172_d", f"{n}\n").split() == [str(exp)]


def test_abc156_d():
    from math import comb

    for n in range(2, 40):
        for _ in range(5):
            a = R.randint(1, n - 1)
            b = R.randint(a + 1, n)
            exp = sum(comb(n, k) for k in range(1, n + 1) if k not in (a, b)) % (10**9 + 7)
            assert run("03/abc156_d", f"{n} {a} {b}\n").split() == [str(exp)]
