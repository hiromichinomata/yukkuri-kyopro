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


# ---------- Part 6 の推奨問題 ----------
def test_agc022_a():
    # 26 文字未満: 末尾に最小の未使用文字。26 文字: 全順列の中で次のもの（小さいアルファベットで同じ規則を確認）
    for _ in range(50):
        s = "".join(R.sample("abcdefghijklmnopqrstuvwxyz", R.randint(1, 25)))
        c = min(ch for ch in "abcdefghijklmnopqrstuvwxyz" if ch not in s)
        assert run("06/agc022_a", s + "\n").split() == [s + c]
    s = "abcdefghijklmnopqrstuvwxyz"
    assert run("06/agc022_a", s + "\n").split() == ["abcdefghijklmnopqrstuvwxz"]  # y を z に替える
    assert run("06/agc022_a", s[::-1] + "\n").split() == ["-1"]


def _arc139_check(n, m, out):
    k, *rest = out.split("\n")
    pts = [tuple(map(int, l.split())) for l in rest if l.strip()]
    assert len(pts) == int(k)
    assert all(1 <= x <= n and 1 <= y <= m for x, y in pts)
    assert len({x + 3 * y for x, y in pts}) == len(pts) == len({3 * x + y for x, y in pts})
    return len(pts)


def test_arc139_c():
    def max_k(n, m):  # 点を辺 (x+3y, 3x+y) とみた二部グラフの最大マッチング
        adj = {}
        for x in range(1, n + 1):
            for y in range(1, m + 1):
                adj.setdefault(x + 3 * y, []).append(3 * x + y)
        match = {}

        def dfs(u, seen):
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    if v not in match or dfs(match[v], seen):
                        match[v] = u
                        return True
            return False

        return sum(dfs(u, set()) for u in adj)

    for n in range(1, 8):
        for m in range(1, 8):
            assert _arc139_check(n, m, run("06/arc139_c", f"{n} {m}\n")) == max_k(n, m)


def test_arc141_c():
    m = load("06/arc141_c")

    def correct(t):
        b = 0
        for c in t:
            b += 1 if c == "(" else -1
            if b < 0:
                return False
        return b == 0

    def brute(s):
        ps = [p for p in itertools.permutations(range(1, len(s) + 1)) if correct("".join(s[i - 1] for i in p))]
        return list(min(ps)), list(max(ps))

    table = {}
    for n in range(1, 4):
        for bits in itertools.product("()", repeat=2 * n):
            s = "".join(bits)
            if s.count("(") == n:
                p, q = brute(s)
                table.setdefault(n, set()).add((tuple(p), tuple(q)))
                out = run("06/arc141_c", f"{n}\n{' '.join(map(str, p))}\n{' '.join(map(str, q))}\n").strip()
                assert out != "-1" and brute(out) == (p, q)
    for _ in range(100):
        n = R.randint(1, 3)
        p, q = list(range(1, 2 * n + 1)), list(range(1, 2 * n + 1))
        R.shuffle(p)
        R.shuffle(q)
        out = run("06/arc141_c", f"{n}\n{' '.join(map(str, p))}\n{' '.join(map(str, q))}\n").strip()
        assert (out != "-1") == ((tuple(p), tuple(q)) in table[n])


def test_arc142_d():
    def brute(n, edges):
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def nxt(S):
            S = sorted(S)
            res = set()
            for choice in itertools.product(*[g[v] for v in S]):
                es = {(min(v, t), max(v, t)) for v, t in zip(S, choice)}
                if len(set(choice)) == len(choice) and len(es) == len(S):
                    res.add(frozenset(choice))
            return next(iter(res)) if len(res) == 1 else None

        cnt = 0
        for mask in range(1, 1 << n):
            S, seen = frozenset(i for i in range(n) if mask >> i & 1), set()
            while S is not None and S not in seen:
                seen.add(S)
                S = nxt(S)
            cnt += S is not None
        return cnt

    for _ in range(60):
        n = R.randint(2, 8)
        edges = [(i, R.randrange(i)) for i in range(1, n)]
        data = f"{n}\n" + "".join(f"{min(a, b) + 1} {max(a, b) + 1}\n" for a, b in edges)
        assert run("06/arc142_d", data).split() == [str(brute(n, edges))]


def test_arc144_c():
    for n in range(2, 9):
        for k in range(1, n):
            exp = next((list(p) for p in itertools.permutations(range(1, n + 1)) if all(abs(p[i] - i - 1) >= k for i in range(n))), None)
            assert run("06/arc144_c", f"{n} {k}\n").split() == (["-1"] if exp is None else list(map(str, exp)))


def test_arc146_d():
    for _ in range(200):
        n, m, k = R.randint(2, 4), R.randint(1, 4), R.randint(1, 4)
        conds = [(*R.sample(range(1, n + 1), 2), R.randint(1, m), R.randint(1, m)) for _ in range(k)]
        best = None
        for a in itertools.product(range(1, m + 1), repeat=n):
            if all((a[p - 1] < x and a[q - 1] < y) or (a[p - 1] == x and a[q - 1] == y) or (a[p - 1] > x and a[q - 1] > y) for p, q, x, y in conds):
                best = sum(a) if best is None else min(best, sum(a))
        data = f"{n} {m} {k}\n" + "".join(f"{p} {x} {q} {y}\n" for p, q, x, y in conds)  # 入力は P X Q Y の順
        assert run("06/arc146_d", data).split() == [str(-1 if best is None else best)]


def test_arc151_d():
    for _ in range(150):
        n, q = R.randint(1, 4), R.randint(1, 8)
        a = [R.randint(0, 9) for _ in range(1 << n)]
        qs = [(R.randrange(n), R.randint(0, 1)) for _ in range(q)]
        b = a[:]
        for x, y in qs:  # 問題文どおり j の小さい順に足していく
            for j in range(1 << n):
                if (j >> x & 1) == y:
                    b[j ^ (1 << x)] += b[j]
        data = f"{n} {q}\n{' '.join(map(str, a))}\n" + "".join(f"{x} {y}\n" for x, y in qs)
        assert run("06/arc151_d", data).split() == [str(v % 998244353) for v in b]


# ---------- Part 7 の推奨問題 ----------
def test_agc017_c():
    def can(arr):
        arr = list(arr)
        while arr:
            nxt = [v for v in arr if v != len(arr)]
            if len(nxt) == len(arr):
                return False
            arr = nxt
        return True

    for _ in range(30):
        n, m = R.randint(1, 5), R.randint(1, 4)
        a = [R.randint(1, n) for _ in range(n)]
        qs = [(R.randint(1, n), R.randint(1, n)) for _ in range(m)]
        goods = [b for b in itertools.product(range(1, n + 1), repeat=n) if can(b)]
        cur, exp = a[:], []
        for x, y in qs:
            cur[x - 1] = y
            exp.append(str(min(sum(u != v for u, v in zip(cur, b)) for b in goods)))
        data = f"{n} {m}\n{' '.join(map(str, a))}\n" + "".join(f"{x} {y}\n" for x, y in qs)
        assert run("07/agc017_c", data).split() == exp


def test_agc018_c():
    for _ in range(80):
        x, y, z = R.randint(1, 3), R.randint(1, 3), R.randint(1, 3)
        ps = [(R.randint(1, 20), R.randint(1, 20), R.randint(1, 20)) for _ in range(x + y + z)]
        best = max(sum(ps[i][c] for i, c in enumerate(asg)) for asg in set(itertools.permutations([0] * x + [1] * y + [2] * z)))
        data = f"{x} {y} {z}\n" + "".join(f"{a} {b} {c}\n" for a, b, c in ps)
        assert run("07/agc018_c", data).split() == [str(best)]


def test_agc021_c():
    import functools

    def feasible(n, m, A, B):
        @functools.lru_cache(None)
        def go(pos, mask, a, b):
            if a == 0 and b == 0:
                return True
            if pos == n * m or 2 * (a + b) > n * m - pos:
                return False
            if mask & 1:
                return go(pos + 1, mask >> 1, a, b)
            i, j = divmod(pos, m)
            return (
                go(pos + 1, mask >> 1, a, b)
                or (a and j + 1 < m and not (mask >> 1 & 1) and go(pos + 1, (mask | 2) >> 1, a - 1, b))
                or (b and i + 1 < n and go(pos + 1, (mask | (1 << m)) >> 1, a, b - 1))
            )

        return go(0, 0, A, B)

    def valid(n, m, A, B, out):
        lines = out.split("\n")
        g = [l for l in lines[1:] if l]
        if lines[0] != "YES" or len(g) != n or any(len(r) != m for r in g):
            return False
        a = b = 0
        for i in range(n):
            for j in range(m):
                c = g[i][j]
                if c == "<":
                    a += 1
                    if j + 1 >= m or g[i][j + 1] != ">":
                        return False
                elif c == "^":
                    b += 1
                    if i + 1 >= n or g[i + 1][j] != "v":
                        return False
                elif c == ">" and (j == 0 or g[i][j - 1] != "<"):
                    return False
                elif c == "v" and (i == 0 or g[i - 1][j] != "^"):
                    return False
        return a == A and b == B

    for n in range(1, 5):
        for m in range(1, 5):
            for A in range(n * m // 2 + 1):
                for B in range(n * m // 2 + 1 - A):
                    out = run("07/agc021_c", f"{n} {m} {A} {B}\n")
                    assert valid(n, m, A, B, out) if feasible(n, m, A, B) else out.strip() == "NO"
    for n, m, A, B in [(3, 3, 2, 2), (5, 5, 6, 6), (5, 7, 8, 9), (7, 7, 12, 12)]:  # 風車が要る形
        assert valid(n, m, A, B, run("07/agc021_c", f"{n} {m} {A} {B}\n"))


def test_agc023_c():
    for n in range(2, 8):
        tot = 0
        for p in itertools.permutations(range(1, n)):
            painted = set()
            for k, mach in enumerate(p, 1):
                painted |= {mach, mach + 1}
                if len(painted) == n:
                    tot += k
                    break
        assert run("07/agc023_c", f"{n}\n").split() == [str(tot % (10**9 + 7))]


def test_arc163_d():
    for n in range(1, 5):
        pairs = list(itertools.combinations(range(n), 2))
        tot = {}
        for bits in itertools.product([0, 1], repeat=len(pairs)):
            reach = [[i == j for j in range(n)] for i in range(n)]
            for (i, j), b in zip(pairs, bits):
                reach[i][j] = reach[i][j] or b == 1
                reach[j][i] = reach[j][i] or b == 0
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
            scc = len({frozenset(j for j in range(n) if reach[i][j] and reach[j][i]) for i in range(n)})
            tot[sum(bits)] = tot.get(sum(bits), 0) + scc
        for m in range(len(pairs) + 1):
            assert run("07/arc163_d", f"{n} {m}\n").split() == [str(tot.get(m, 0))]


def test_arc165_e():
    from fractions import Fraction
    from functools import lru_cache

    MOD = 998244353
    for _ in range(25):
        n, edges = R.randint(2, 6), None
        k = R.randint(1, n - 1)
        edges = [(i, R.randrange(i)) for i in range(1, n)]

        @lru_cache(None)
        def E(removed):
            rem = set(removed)
            comp, sizes = {}, []
            for s in range(n):
                if s in comp:
                    continue
                st, comp[s], cnt = [s], len(sizes), 0
                while st:
                    v = st.pop()
                    cnt += 1
                    for a, b in edges:
                        if a in rem or b in rem:
                            continue
                        for x, y in ((a, b), (b, a)):
                            if x == v and y not in comp:
                                comp[y] = comp[s]
                                st.append(y)
                sizes.append(cnt)
            cand = [v for v in range(n) if sizes[comp[v]] >= k + 1]
            if not cand:
                return Fraction(0)
            return 1 + sum(E(tuple(sorted(rem | {v}))) for v in cand) / len(cand)

        e = E(())
        exp = e.numerator % MOD * pow(e.denominator, MOD - 2, MOD) % MOD
        data = f"{n} {k}\n" + "".join(f"{a + 1} {b + 1}\n" for a, b in edges)
        assert run("07/arc165_e", data).split() == [str(exp)]


def test_arc166_e():
    cases = [(R.randint(1, 3), *sorted(R.sample(range(1, 7), 2))) for _ in range(60)]
    out = run("07/arc166_e", f"{len(cases)}\n" + "".join(f"{n} {a} {b}\n" for n, a, b in cases)).split()
    for idx, (n, a, b) in enumerate(cases):
        gl, gr = int(out[2 * idx]), int(out[2 * idx + 1])
        lim, best = 3 * gr + a * b + 10, None
        for L in range(1, lim):
            cnt = 0
            for Rr in range(L, lim):
                cnt += (Rr % a == 0) - (Rr % b == 0)
                if cnt == n and (best is None or Rr - L > best[1] - best[0]):
                    best = (L, Rr)
        assert (gl, gr) == best


def test_arc167_e():
    def inside(p, t):
        def cr(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        d = (cr(t[0], t[1], p), cr(t[1], t[2], p), cr(t[2], t[0], p))
        return all(x >= 0 for x in d) or all(x <= 0 for x in d)

    ss = list(range(1, 120))
    out = run("07/arc167_e", f"{len(ss)}\n" + "".join(f"{s}\n" for s in ss)).split("\n")
    it = iter(out)
    for s in ss:
        if next(it) == "No":
            assert s in (1, 2, 3, 5, 7)
            continue
        v = list(map(int, next(it).split()))
        t = [(v[0], v[1]), (v[2], v[3]), (v[4], v[5])]
        assert abs((t[1][0] - t[0][0]) * (t[2][1] - t[0][1]) - (t[1][1] - t[0][1]) * (t[2][0] - t[0][0])) == s
        xs, ys = [p[0] for p in t], [p[1] for p in t]
        squares = sum(
            all(inside(q, t) for q in ((x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)))
            for x in range(min(xs), max(xs))
            for y in range(min(ys), max(ys))
        )
        assert squares == 1
