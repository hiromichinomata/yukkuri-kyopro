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
    # sys.stdin.buffer から読む解答もあるので、バイト列の上に文字列のラッパーをかぶせる
    sys.stdin, sys.stdout = io.TextIOWrapper(io.BytesIO(data.encode())), io.StringIO()
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


# ---------- Part 4 の推奨問題 ----------
def test_abc035_c():
    for _ in range(100):
        n = R.randint(1, 10)
        ops = [(lambda l: (l, R.randint(l, n)))(R.randint(1, n)) for _ in range(R.randint(1, 8))]
        s = [0] * n
        for l, r in ops:
            for i in range(l - 1, r):
                s[i] ^= 1
        data = f"{n} {len(ops)}\n" + "".join(f"{l} {r}\n" for l, r in ops)
        assert run("04/abc035_c", data).split() == ["".join(map(str, s))]


def test_abc147_d():
    for _ in range(100):
        a = [R.randint(0, 2**60 - 1) for _ in range(R.randint(2, 8))]
        exp = sum(x ^ y for x, y in itertools.combinations(a, 2)) % (10**9 + 7)
        assert run("04/abc147_d", f"{len(a)}\n{' '.join(map(str, a))}\n").split() == [str(exp)]


def test_abc154_e():
    for n in list(range(1, 300)) + [R.randint(1, 10**5) for _ in range(20)]:
        for k in (1, 2, 3):
            exp = sum(1 for x in range(1, n + 1) if sum(c != "0" for c in str(x)) == k)
            assert run("04/abc154_e", f"{n}\n{k}\n").split() == [str(exp)]


def test_abc180_e():
    for _ in range(40):
        n = R.randint(2, 6)
        p = list({(R.randint(-5, 5), R.randint(-5, 5), R.randint(-5, 5)) for _ in range(n)})
        n = len(p)
        if n < 2:
            continue
        c = lambda a, b: abs(b[0] - a[0]) + abs(b[1] - a[1]) + max(0, b[2] - a[2])
        exp = min(
            sum(c(p[o[i]], p[o[i + 1]]) for i in range(n))
            for rest in itertools.permutations(range(1, n))
            for o in [(0,) + rest + (0,)]
        )
        data = f"{n}\n" + "".join(f"{x} {y} {z}\n" for x, y, z in p)
        assert run("04/abc180_e", data).split() == [str(exp)]


def test_abc184_e():
    from collections import deque as dq

    for _ in range(100):
        h, w = R.randint(1, 5), R.randint(2, 5)
        cells = [R.choice(".#ab") for _ in range(h * w)]
        s, g = R.sample(range(h * w), 2)
        cells[s], cells[g] = "S", "G"
        # 愚直: テレポートも普通の辺として張った BFS
        dist = [-1] * (h * w)
        dist[s] = 0
        q = dq([s])
        while q:
            v = q.popleft()
            i, j = divmod(v, w)
            nb = [(i + di) * w + j + dj for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= i + di < h and 0 <= j + dj < w]
            if cells[v] in "ab":
                nb += [u for u in range(h * w) if cells[u] == cells[v]]
            for u in nb:
                if dist[u] == -1 and cells[u] != "#":
                    dist[u] = dist[v] + 1
                    q.append(u)
        data = f"{h} {w}\n" + "\n".join("".join(cells[i * w : (i + 1) * w]) for i in range(h)) + "\n"
        assert run("04/abc184_e", data).split() == [str(dist[g])]


def test_abc187_e():
    for _ in range(100):
        n = R.randint(2, 8)
        edges = [(i + 1, R.randint(1, i)) for i in range(1, n)]
        R.shuffle(edges)
        edges = [(a, b) if R.random() < 0.5 else (b, a) for a, b in edges]
        g = [[] for _ in range(n + 1)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        qs = [(R.randint(1, 2), R.randint(1, n - 1), R.randint(1, 9)) for _ in range(R.randint(1, 6))]
        c = [0] * (n + 1)
        for t, e, x in qs:
            a, b = edges[e - 1]
            if t == 2:
                a, b = b, a
            seen, stack = {a, b}, [a]
            while stack:
                v = stack.pop()
                c[v] += x
                for to in g[v]:
                    if to not in seen:
                        seen.add(to)
                        stack.append(to)
        data = f"{n}\n" + "".join(f"{a} {b}\n" for a, b in edges) + f"{len(qs)}\n" + "".join(f"{t} {e} {x}\n" for t, e, x in qs)
        assert run("04/abc187_e", data).split() == list(map(str, c[1:]))


def test_abc199_d():
    for _ in range(100):
        n = R.randint(1, 7)
        es = sorted({tuple(sorted(R.sample(range(1, n + 1), 2))) for _ in range(R.randint(0, 10))} if n >= 2 else set())
        exp = sum(all(col[a - 1] != col[b - 1] for a, b in es) for col in itertools.product(range(3), repeat=n))
        data = f"{n} {len(es)}\n" + "".join(f"{a} {b}\n" for a, b in es)
        assert run("04/abc199_d", data).split() == [str(exp)]


def test_arc118_a():
    for t in range(1, 51):
        prices = {(100 + t) * a // 100 for a in range(1, 2000)}
        missing = [v for v in range(1, (100 + t) * 1999 // 100) if v not in prices]
        for n in (1, 2, t, t + 1, 3 * t + 2):
            assert run("04/arc118_a", f"{t} {n}\n").split() == [str(missing[n - 1])]


def test_dp_s():
    for _ in range(100):
        k = R.randint(1, 3000)
        d = R.randint(1, 30)
        exp = sum(1 for x in range(1, k + 1) if sum(map(int, str(x))) % d == 0) % (10**9 + 7)
        assert run("04/dp_s", f"{k}\n{d}\n").split() == [str(exp)]


# ---------- Part 5 の推奨問題 ----------
def test_abc214_f():
    for _ in range(200):
        s = "".join(R.choice("abc") for _ in range(R.randint(1, 10)))
        n = len(s)
        ts = {"".join(s[i] for i in range(n) if mask >> i & 1) for mask in range(1, 1 << n) if not mask & (mask >> 1)}
        assert run("05/abc214_f", s + "\n").split() == [str(len(ts) % (10**9 + 7))]


def test_abc256_d():
    for _ in range(200):
        iv = [(lambda l: (l, R.randint(l + 1, 12)))(R.randint(1, 11)) for _ in range(R.randint(1, 6))]
        covered = [any(l <= x < r for l, r in iv) for x in range(14)]
        exp = []
        x = 0
        while x < 14:
            if covered[x]:
                y = x
                while y < 14 and covered[y]:
                    y += 1
                exp += [str(x), str(y)]
                x = y
            else:
                x += 1
        data = f"{len(iv)}\n" + "".join(f"{l} {r}\n" for l, r in iv)
        assert run("05/abc256_d", data).split() == exp


def test_abc240_f():
    for _ in range(200):
        n = R.randint(1, 5)
        runs = [(R.randint(-4, 4), R.randint(1, 6)) for _ in range(n)]
        c = [x for x, y in runs for _ in range(y)]
        b = a = 0
        best = None
        for v in c:
            b += v
            a += b
            best = a if best is None else max(best, a)
        data = f"1\n{n} {len(c)}\n" + "".join(f"{x} {y}\n" for x, y in runs)
        assert run("05/abc240_f", data).split() == [str(best)]


def test_abc229_d():
    for _ in range(200):
        s = "".join(R.choice("X.") for _ in range(R.randint(1, 12)))
        k = R.randint(0, 5)
        exp = max(r - l for l in range(len(s)) for r in range(l, len(s) + 1) if s[l:r].count(".") <= k)
        assert run("05/abc229_d", f"{s}\n{k}\n").split() == [str(exp)]


def test_arc151_b():
    for _ in range(100):
        n, m = R.randint(1, 5), R.randint(1, 4)
        p = list(range(1, n + 1))
        R.shuffle(p)
        exp = sum(1 for a in itertools.product(range(1, m + 1), repeat=n) if list(a) < [a[x - 1] for x in p])
        assert run("05/arc151_b", f"{n} {m}\n{' '.join(map(str, p))}\n").split() == [str(exp % 998244353)]
