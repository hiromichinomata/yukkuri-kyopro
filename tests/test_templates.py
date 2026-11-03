"""本文テンプレート（Python）を小さいランダム入力で愚直解と比べるテスト。"""

import itertools
import random
from collections import deque

import pytest
from conftest import load

R = random.Random(20261103)
TRIALS = 200


def rand_graph(n, m, directed=False):
    es = set()
    for _ in range(m):
        u, v = R.randrange(n), R.randrange(n)
        if u != v:
            es.add((u, v) if directed else (min(u, v), max(u, v)))
    return sorted(es)


# ---------- Part 4 ----------
def test_bfs01():
    m = load("04/bfs01")
    for _ in range(TRIALS):
        n = R.randint(1, 7)
        g = [[] for _ in range(n)]
        es = [(R.randrange(n), R.randrange(n), R.randint(0, 1)) for _ in range(R.randint(0, 15))]
        for u, v, c in es:
            g[u].append((v, c))
        INF = 10**18
        d = [INF] * n
        d[0] = 0
        for _ in range(n):  # ベルマンフォード
            for u, v, c in es:
                if d[u] + c < d[v]:
                    d[v] = d[u] + c
        assert m.bfs01(g, 0, n) == d


def test_bipartite():
    m = load("04/bipartite")
    for _ in range(TRIALS):
        n = R.randint(1, 7)
        es = rand_graph(n, R.randint(0, 10))
        g = [[] for _ in range(n)]
        for u, v in es:
            g[u].append(v)
            g[v].append(u)
        brute = any(all(c[u] != c[v] for u, v in es) for c in itertools.product([0, 1], repeat=n))
        assert m.is_bipartite(g, n) == brute


def test_tsp_path():
    m = load("04/dp_bitmask")
    for _ in range(50):
        n = R.randint(1, 6)
        dist = [[0 if i == j else R.randint(1, 20) for j in range(n)] for i in range(n)]
        brute = min(
            sum(dist[p[i]][p[i + 1]] for i in range(n - 1))
            for p in itertools.permutations(range(n))
            if p[0] == 0
        )
        assert m.tsp(dist, n) == brute


def test_merge_stones():
    m = load("04/dp_interval")
    from functools import lru_cache

    for _ in range(TRIALS):
        a = [R.randint(1, 9) for _ in range(R.randint(1, 7))]

        @lru_cache(None)
        def f(l, r):
            if l == r:
                return 0
            return min(f(l, k) + f(k + 1, r) for k in range(l, r)) + sum(a[l : r + 1])

        assert m.merge_stones(a) == f(0, len(a) - 1)


def test_fenwick_segtree():
    fw = load("04/fenwick")
    sg = load("04/segtree")
    for _ in range(50):
        n = R.randint(1, 20)
        a = [R.randint(-5, 5) for _ in range(n)]
        f = fw.Fenwick(n)
        for i, v in enumerate(a, 1):
            f.add(i, v)
        s = sg.SegTree(a)
        for _ in range(50):
            i = R.randrange(n)
            x = R.randint(-5, 5)
            f.add(i + 1, x - a[i])
            s.update(i, x)
            a[i] = x
            l = R.randrange(n)
            r = R.randint(l + 1, n)
            assert f.range_sum(l + 1, r) == sum(a[l:r])
            assert s.query(l, r) == sum(a[l:r])


def test_floyd():
    m = load("04/floyd_warshall")
    INF = 10**17
    for _ in range(TRIALS):
        n = R.randint(1, 6)
        d = [[0 if i == j else (R.randint(1, 9) if R.random() < 0.4 else INF) for j in range(n)] for i in range(n)]
        bf = [row[:] for row in d]
        for _ in range(n):
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        if bf[i][k] + d[k][j] < bf[i][j]:
                            bf[i][j] = bf[i][k] + d[k][j]
        bf = [[x if x < INF else INF for x in row] for row in bf]
        assert m.floyd([row[:] for row in d]) == bf


def test_ncr():
    m = load("04/modinv")
    from math import comb

    fac, inv = m.prepare_fac(60)
    for n in range(61):
        for r in range(-1, n + 2):
            exp = comb(n, r) % m.MOD if 0 <= r <= n else 0
            assert m.ncr(n, r, fac, inv) == exp


def test_prefix_sum_2d():
    m = load("04/prefix_sum_2d")
    for _ in range(TRIALS):
        h, w = R.randint(1, 5), R.randint(1, 5)
        a = [[R.randint(-9, 9) for _ in range(w)] for _ in range(h)]
        s = m.build_2d(a)
        h1, h2 = sorted([R.randint(1, h), R.randint(1, h)])
        w1, w2 = sorted([R.randint(1, w), R.randint(1, w)])
        exp = sum(a[i][j] for i in range(h1 - 1, h2) for j in range(w1 - 1, w2))
        assert m.rect_sum(s, h1, w1, h2, w2) == exp


def test_two_pointers():
    m = load("04/two_pointers")
    for _ in range(TRIALS):
        xs = [R.randint(0, 6) for _ in range(R.randint(0, 8))]
        k = R.randint(0, 12)
        exp = sum(1 for l in range(len(xs)) for r in range(l, len(xs)) if sum(xs[l : r + 1]) <= k)
        assert m.count_subarray_le_k(xs, k) == exp


# ---------- Part 5 ----------
def test_convex_hull():
    m = load("05/convex_hull")
    for _ in range(TRIALS):
        pts = [(R.randint(0, 5), R.randint(0, 5)) for _ in range(R.randint(1, 10))]
        hull = m.convex_hull(pts)
        hs = set(hull)
        uniq = set(pts)
        # 凸包の頂点 = どの 3 点の三角形・2 点の線分の内部（端点以外）にも入らない点
        def strictly_inside_some(p):
            others = [q for q in uniq if q != p]
            for a, b in itertools.combinations(others, 2):
                if m.ccw(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]):
                    return True
            for a, b, c in itertools.combinations(others, 3):
                s1, s2, s3 = m.ccw(a, b, p), m.ccw(b, c, p), m.ccw(c, a, p)
                if m.ccw(a, b, c) != 0 and ((s1 >= 0 and s2 >= 0 and s3 >= 0) or (s1 <= 0 and s2 <= 0 and s3 <= 0)):
                    return True
            return False

        exp = {p for p in uniq if not strictly_inside_some(p)}
        if len(uniq) == 1:
            exp = uniq
        assert hs == exp
        assert len(hull) == len(hs)


def test_kmp_z():
    km = load("05/kmp")
    za = load("05/z_algorithm")
    for _ in range(TRIALS):
        t = "".join(R.choice("ab") for _ in range(R.randint(1, 12)))
        p = "".join(R.choice("ab") for _ in range(R.randint(1, 4)))
        assert km.kmp_search(t, p) == [i for i in range(len(t) - len(p) + 1) if t[i : i + len(p)] == p]
        z = za.z_algorithm(t)
        for i in range(1, len(t)):
            k = 0
            while i + k < len(t) and t[k] == t[i + k]:
                k += 1
            assert z[i] == k


def test_kruskal():
    m = load("05/kruskal")
    for _ in range(TRIALS):
        n = R.randint(1, 5)
        es = [(u, v, R.randint(1, 9)) for u, v in rand_graph(n, 8)]
        # 連結でなければ最小全域森の重み
        best = None
        for k in range(len(es) + 1):
            for sub in itertools.combinations(es, k):
                d = m.DSU(n)
                if all(d.unite(u, v) for u, v, _ in sub):
                    comps = len({d.find(i) for i in range(n)})
                    full = m.DSU(n)
                    for u, v, _ in es:
                        full.unite(u, v)
                    if comps == len({full.find(i) for i in range(n)}):
                        w = sum(c for *_, c in sub)
                        best = w if best is None else min(best, w)
        assert m.kruskal(n, es[:]) == best


def test_lcs_lis():
    lc = load("05/lcs")
    li = load("05/lis_fast")
    for _ in range(TRIALS):
        s = "".join(R.choice("abc") for _ in range(R.randint(0, 6)))
        t = "".join(R.choice("abc") for _ in range(R.randint(0, 6)))
        best = 0
        for k in range(len(s) + 1):
            for idx in itertools.combinations(range(len(s)), k):
                sub = "".join(s[i] for i in idx)
                it = iter(t)
                if all(c in it for c in sub):
                    best = max(best, k)
        assert lc.lcs(s, t) == best
        a = [R.randint(0, 5) for _ in range(R.randint(0, 8))]
        exp = max(
            (k for k in range(len(a) + 1) for idx in itertools.combinations(range(len(a)), k) if all(a[idx[i]] < a[idx[i + 1]] for i in range(k - 1))),
            default=0,
        )
        assert li.lis_length(a) == exp


def _min_cut(n, es, s, t):
    best = None
    for mask in range(1 << n):
        if not (mask >> s & 1) or (mask >> t & 1):
            continue
        c = sum(w for u, v, w in es if (mask >> u & 1) and not (mask >> v & 1))
        best = c if best is None else min(best, c)
    return best


def test_max_flow_dinic():
    mf = load("05/max_flow")
    dn = load("06/dinic")
    for _ in range(TRIALS):
        n = R.randint(2, 6)
        es = [(u, v, R.randint(1, 9)) for u, v in rand_graph(n, 12, directed=True)]
        exp = _min_cut(n, es, 0, n - 1)
        cap = [[0] * n for _ in range(n)]
        d = dn.Dinic(n)
        for u, v, w in es:
            cap[u][v] += w
            d.add_edge(u, v, w)
        assert mf.max_flow(cap, 0, n - 1, n) == exp
        assert d.max_flow(0, n - 1) == exp


def test_lazy_segtree():
    m = load("05/segtree_lazy")
    for _ in range(50):
        n = R.randint(1, 16)
        a = [R.randint(-5, 5) for _ in range(n)]
        st = m.LazySegTree(a)
        for _ in range(60):
            l = R.randrange(n)
            r = R.randint(l + 1, n)
            if R.random() < 0.5:
                x = R.randint(-5, 5)
                st.range_add(l, r, x)
                for i in range(l, r):
                    a[i] += x
            else:
                assert st.range_sum(l, r) == sum(a[l:r])


# ---------- Part 6 ----------
def test_aho_corasick():
    m = load("06/aho_corasick")
    for _ in range(TRIALS):
        words = list({"".join(R.choice("ab") for _ in range(R.randint(1, 3))) for _ in range(R.randint(1, 4))})
        text = "".join(R.choice("ab") for _ in range(R.randint(0, 12)))
        ac = m.AhoCorasick()
        for w in words:
            ac.add(w)
        ac.build()
        exp = sorted((i + len(w) - 1, w) for w in words for i in range(len(text) - len(w) + 1) if text[i : i + len(w)] == w)
        assert sorted(ac.search(text)) == exp


def test_cht():
    m = load("06/cht")
    for _ in range(TRIALS):
        lines = sorted({(R.randint(-6, 6), R.randint(-10, 10)) for _ in range(R.randint(1, 6))}, key=lambda l: (-l[0], l[1]))
        dq = m.cht_min(lines)
        for x in range(-6, 7):
            assert m.query(dq, x) == min(a * x + b for a, b in lines)


def test_inclusion_exclusion():
    m = load("06/inclusion_exclusion")
    for n in range(0, 100):
        assert m.count_coprime(n) == sum(1 for i in range(1, n + 1) if i % 2 and i % 3)


def test_fib():
    m = load("06/matrix_pow")
    a, b = 0, 1
    for n in range(60):
        assert m.fib(n) == a % m.MOD
        a, b = b, a + b


def test_mo():
    m = load("06/mo")
    for _ in range(TRIALS):
        a = [R.randint(0, 4) for _ in range(R.randint(1, 15))]
        n = len(a)
        qs = []
        for _ in range(R.randint(1, 8)):
            l = R.randrange(n)
            qs.append((l, R.randint(l, n - 1)))
        assert m.mo_count_distinct(a, qs) == [len(set(a[l : r + 1])) for l, r in qs]


def test_ntt_convolution():
    for mod_name, fn in [("06/ntt", "convolution"), ("08/convolution", "conv")]:
        m = load(mod_name)
        for _ in range(100):
            a = [R.randint(0, 50) for _ in range(R.randint(1, 9))]
            b = [R.randint(0, 50) for _ in range(R.randint(1, 9))]
            exp = [0] * (len(a) + len(b) - 1)
            for i, x in enumerate(a):
                for j, y in enumerate(b):
                    exp[i + j] += x * y
            assert getattr(m, fn)(a, b) == exp, mod_name


def test_suffix_array():
    m = load("06/suffix_array")
    for _ in range(TRIALS):
        s = "".join(R.choice("ab") for _ in range(R.randint(1, 12)))
        assert m.suffix_array(s) == sorted(range(len(s)), key=lambda i: s[i:])


# ---------- Part 7 ----------
def test_closest_pair():
    m = load("07/closest_pair")
    for _ in range(TRIALS):
        pts = [(R.randint(0, 30), R.randint(0, 30)) for _ in range(R.randint(2, 20))]
        exp = min(m.dist2(p, q) for p, q in itertools.combinations(pts, 2))
        assert m.closest_pair(pts) == exp


def test_bsgs():
    m = load("07/discrete_log")
    for p in [5, 7, 11, 13, 101]:
        for a in range(1, p):
            for b in range(1, p):
                exp = next((x for x in range(p - 1) if pow(a, x, p) == b), -1)
                assert m.bsgs(a, b, p, p - 1) == exp, (a, b, p)


def test_gauss():
    m = load("07/gauss")
    p = m.MOD
    for _ in range(TRIALS):
        n = R.randint(1, 4)
        A = [[R.randint(0, 3) for _ in range(n)] for _ in range(n)]
        x = [R.randint(0, 5) for _ in range(n)]
        aug = [row + [sum(row[j] * x[j] for j in range(n)) % p] for row in A]
        res = m.gauss([r[:] for r in aug])
        # 簡約後の連立方程式を、元の解 x が満たすこと／ピボット行が単位ベクトルになっていること
        for row in res:
            assert sum(row[j] * x[j] for j in range(n)) % p == row[n] % p
        piv = [next((j for j in range(n) if row[j]), None) for row in res]
        for i, j in enumerate(piv):
            if j is not None:
                assert res[i][j] == 1 and all(res[k][j] == 0 for k in range(len(res)) if k != i)


def test_meet_in_middle_branch_bound():
    mm = load("07/meet_in_middle")
    bb = load("08/branch_bound")
    for _ in range(TRIALS):
        xs = [R.randint(1, 15) for _ in range(R.randint(0, 8))]
        t = R.randint(0, 40)
        exp = any(sum(c) == t for k in range(len(xs) + 1) for c in itertools.combinations(xs, k))
        assert mm.can_make_sum(xs, t) == exp
        assert bb.subset_sum_pruned(xs, t) == exp


def test_persistent_segtree():
    m = load("07/persistent_segtree")
    for _ in range(50):
        n = R.randint(1, 10)
        arr = [R.randint(0, 9) for _ in range(n)]
        roots = [m.build(0, n - 1, arr)]
        vers = [arr[:]]
        for _ in range(20):
            v = R.randrange(len(roots))
            i, d = R.randrange(n), R.randint(-5, 5)
            roots.append(m.update(roots[v], 0, n - 1, i, d))
            nv = vers[v][:]
            nv[i] += d
            vers.append(nv)
            k = R.randrange(len(roots))
            l = R.randrange(n)
            r = R.randint(l, n - 1)
            assert m.query(roots[k], 0, n - 1, l, r) == sum(vers[k][l : r + 1])


def test_scc_sat2():
    sc = load("07/scc")
    s2 = load("07/sat2")
    for _ in range(TRIALS):
        n = R.randint(1, 7)
        es = rand_graph(n, 12, directed=True)
        g = [[] for _ in range(n)]
        for u, v in es:
            g[u].append(v)
        reach = [[i == j for j in range(n)] for i in range(n)]
        for u, v in es:
            reach[u][v] = True
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    reach[i][j] |= reach[i][k] and reach[k][j]
        comp, k = sc.scc(g, n)
        for i in range(n):
            for j in range(n):
                assert (comp[i] == comp[j]) == (reach[i][j] and reach[j][i])
        # 縮約後の番号はトポロジカル順（辺 u→v なら comp[u] <= comp[v]）
        for u, v in es:
            assert comp[u] <= comp[v]
    for _ in range(TRIALS):
        nv = R.randint(1, 4)
        clauses = [(R.randrange(2 * nv), R.randrange(2 * nv)) for _ in range(R.randint(1, 6))]
        # 節 (a ∨ b) → ¬a ⇒ b, ¬b ⇒ a。リテラル 2i = x_i, 2i+1 = ¬x_i
        imp = []
        for a, b in clauses:
            s2.add_clause(imp, a, b)
        val = lambda lit, asg: asg[lit // 2] ^ (lit & 1)
        exp = any(all(val(a, asg) or val(b, asg) for a, b in clauses) for asg in itertools.product([0, 1], repeat=nv))
        assert s2.sat2_solvable(imp, nv) == exp


def test_xor_basis():
    m = load("07/xor_basis")
    for _ in range(TRIALS):
        xs = [R.randint(0, 63) for _ in range(R.randint(0, 6))]
        b = m.XorBasis(bits=8)
        for x in xs:
            b.add(x)
        exp = 0
        for k in range(len(xs) + 1):
            for c in itertools.combinations(xs, k):
                v = 0
                for x in c:
                    v ^= x
                exp = max(exp, v)
        assert b.max_xor() == exp


# ---------- Part 8 ----------
def test_monoid_seg():
    m = load("08/monoid_seg")
    for _ in range(50):
        n = R.randint(1, 12)
        a = [R.randint(-9, 9) for _ in range(n)]
        mx = m.MonoidSeg(a, max, -(10**30))
        cat = m.MonoidSeg([str(x) + "," for x in a], lambda x, y: x + y, "")  # 非可換
        for _ in range(40):
            i, x = R.randrange(n), R.randint(-9, 9)
            a[i] = x
            mx.update(i, x)
            cat.update(i, str(x) + ",")
            l = R.randrange(n)
            r = R.randint(l + 1, n)
            assert mx.query(l, r) == max(a[l:r])
            assert cat.query(l, r) == "".join(str(v) + "," for v in a[l:r])


def test_segbeats():
    m = load("08/segbeats")
    for _ in range(100):
        n = R.randint(1, 10)
        a = [R.randint(0, 20) for _ in range(n)]
        st = m.SegBeats(a)
        for _ in range(30):
            l = R.randrange(n)
            r = R.randint(l, n - 1)
            if R.random() < 0.5:
                x = R.randint(0, 20)
                st.range_chmin(l, r, x)
                for i in range(l, r + 1):
                    a[i] = min(a[i], x)
            else:
                assert st.range_sum(l, r) == sum(a[l : r + 1])


def _rand_tree(n):
    par = [-1] + [R.randrange(v) if R.random() < 0.3 else v - 1 for v in range(1, n)]  # 細長い木も作る
    g = [[] for _ in range(n)]
    for v in range(1, n):
        g[v].append(par[v])
        g[par[v]].append(v)
    return par, g


def _naive_lca(par, a, b):
    anc = set()
    while a != -1:
        anc.add(a)
        a = par[a]
    while b not in anc:
        b = par[b]
    return b


def test_lca_hld():
    lc = load("06/lca")
    hl = load("07/hld")
    for _ in range(TRIALS):
        n = R.randint(1, 40)
        par, g = _rand_tree(n)
        depth, up, LOG = lc.build_lca(g)
        hpar, hdepth, head, pos = hl.build_hld(g)
        assert sorted(pos) == list(range(n))
        for _ in range(20):
            a, b = R.randrange(n), R.randrange(n)
            exp = _naive_lca(par, a, b)
            assert lc.lca(a, b, depth, up, LOG) == exp
            assert hl.hld_lca(a, b, hpar, hdepth, head) == exp


# ---------- Part 3 ----------
def test_dijkstra():
    m = load("03/dijkstra")
    for _ in range(TRIALS):
        n = R.randint(1, 7)
        es = [(R.randrange(n), R.randrange(n), R.randint(0, 9)) for _ in range(R.randint(0, 15))]
        g = [[] for _ in range(n)]
        for u, v, c in es:
            g[u].append((v, c))
        INF = 10**18
        d = [INF] * n
        d[0] = 0
        for _ in range(n):
            for u, v, c in es:
                if d[u] + c < d[v]:
                    d[v] = d[u] + c
        assert m.dijkstra(g, 0, n) == d


def test_deque_window():
    m = load("03/deque_window")
    for _ in range(TRIALS):
        xs = [R.randint(-9, 9) for _ in range(R.randint(1, 10))]
        k = R.randint(1, len(xs))
        assert m.max_sum_k(xs, k) == max(sum(xs[i : i + k]) for i in range(len(xs) - k + 1))


def test_knapsack_lis():
    kn = load("03/knapsack")
    li = load("03/lis")
    for _ in range(TRIALS):
        n = R.randint(0, 6)
        ws = [R.randint(1, 6) for _ in range(n)]
        vs = [R.randint(1, 9) for _ in range(n)]
        cap = R.randint(0, 15)
        exp = max(sum(vs[i] for i in c) for k in range(n + 1) for c in itertools.combinations(range(n), k) if sum(ws[i] for i in c) <= cap)
        assert kn.knapsack(ws, vs, cap) == exp
        a = [R.randint(0, 5) for _ in range(R.randint(1, 8))]
        exp = max(k for k in range(1, len(a) + 1) for idx in itertools.combinations(range(len(a)), k) if all(a[idx[i]] < a[idx[i + 1]] for i in range(k - 1)))
        assert li.lis(a) == exp


def test_ncr_pascal():
    m = load("03/ncr")
    from math import comb

    c = m.build_ncr(40)
    for n in range(41):
        for r in range(n + 1):
            assert c[n][r] == comb(n, r) % m.MOD


def test_topological_sort():
    m = load("03/topological_sort")
    for _ in range(TRIALS):
        n = R.randint(1, 7)
        perm = list(range(n))
        R.shuffle(perm)
        es = {(perm[i], perm[j]) for i in range(n) for j in range(i + 1, n) if R.random() < 0.3}
        g = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in es:
            g[u].append(v)
            indeg[v] += 1
        order = m.topological_sort(n, g, indeg)
        assert sorted(order) == list(range(n))
        where = {v: i for i, v in enumerate(order)}
        assert all(where[u] < where[v] for u, v in es)
        # 閉路があると全頂点は出てこない
        if n >= 2:
            g2 = [row[:] for row in g]
            g2[0].append(1)
            g2[1].append(0)
            indeg2 = [0] * n
            for u in range(n):
                for v in g2[u]:
                    indeg2[v] += 1
            assert len(m.topological_sort(n, g2, indeg2)) < n


def test_dsu_paths_grid():
    ds = load("03/dsu")
    dp = load("03/dp_paths")
    gd = load("03/grid_dfs")
    for _ in range(TRIALS):
        n = R.randint(1, 8)
        d = ds.DSU(n)
        es = rand_graph(n, R.randint(0, 8))
        for u, v in es:
            d.unite(u, v)
        reach = [[i == j for j in range(n)] for i in range(n)]
        for u, v in es:
            reach[u][v] = reach[v][u] = True
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    reach[i][j] |= reach[i][k] and reach[k][j]
        for i in range(n):
            assert d.size[d.find(i)] == sum(reach[i])
            for j in range(n):
                assert d.same(i, j) == reach[i][j]
        h, w = R.randint(1, 4), R.randint(1, 4)
        blocked = [[R.random() < 0.25 for _ in range(w)] for _ in range(h)]

        def cnt(i, j):
            if i >= h or j >= w or blocked[i][j]:
                return 0
            if (i, j) == (h - 1, w - 1):
                return 1
            return cnt(i + 1, j) + cnt(i, j + 1)

        assert dp.paths(h, w, blocked) == cnt(0, 0)
        grid = ["".join("#" if blocked[i][j] else "." for j in range(w)) for i in range(h)]
        free = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == "."]
        if free:
            si, sj = free[0]
            seen = [[False] * w for _ in range(h)]
            comp, q = {(si, sj)}, deque([(si, sj)])
            while q:
                i, j = q.popleft()
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == "." and (ni, nj) not in comp:
                        comp.add((ni, nj))
                        q.append((ni, nj))
            assert gd.dfs(si, sj, grid, seen) == len(comp)


def test_lower_bound():
    m = load("03/lower_bound")
    import bisect

    for _ in range(TRIALS):
        a = sorted(R.randint(0, 9) for _ in range(R.randint(0, 10)))
        x = R.randint(-1, 10)
        assert m.lower_bound(a, x) == bisect.bisect_left(a, x)
