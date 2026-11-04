import sys


def greedy(s: str, largest: bool) -> list:
    """S から、S_p が正しい括弧列になる順列 p のうち辞書順最小（largest なら最大）を作る。
    残高が 0 のときは「(」しか取れない。それ以外は好きな文字を取れるので、
    使っていない添字の最小（最大）を取ればよい（残りは必ず正しく並べ切れる）"""
    n2 = len(s)
    order = range(n2 - 1, -1, -1) if largest else range(n2)
    all_idx = list(order)  # 添字の候補を、取りたい順に並べたもの
    open_idx = [i for i in all_idx if s[i] == "("]
    used = [False] * n2
    pa = po = 0  # all_idx・open_idx の先頭（使用済みは読み飛ばす）
    bal = 0
    res = []
    for _ in range(n2):
        if bal == 0:
            while used[open_idx[po]]:
                po += 1
            i = open_idx[po]
        else:
            while used[all_idx[pa]]:
                pa += 1
            i = all_idx[pa]
        used[i] = True
        bal += 1 if s[i] == "(" else -1
        res.append(i + 1)
    return res


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    s = [""] * (2 * n)

    def force(i, c):
        if s[i] and s[i] != c:
            return False
        s[i] = c
        return True

    ok = True
    for k in range(0, 2 * n, 2):
        # 最小の P で、隣り合う 2 つが「大きい添字 → 小さい添字」の順なら、それは「(」→「)」と決まる
        # （そうでなければ入れ替えた方が辞書順で小さく、しかも正しい括弧列のまま）
        if p[k] > p[k + 1]:
            ok &= force(p[k] - 1, "(") and force(p[k + 1] - 1, ")")
        # 最大の Q では逆に「小さい → 大きい」の順のとき
        if q[k] < q[k + 1]:
            ok &= force(q[k] - 1, "(") and force(q[k + 1] - 1, ")")
    # 決まらない位置が残る・矛盾する・個数が合わないなら、条件を満たす S はない
    if not ok or "" in s or s.count("(") != n:
        print(-1)
        return
    t = "".join(s)
    # 決めた S から最小・最大の順列を作り直し、入力と一致するか確かめる
    print(t if greedy(t, False) == p and greedy(t, True) == q else -1)


if __name__ == "__main__":
    main()
