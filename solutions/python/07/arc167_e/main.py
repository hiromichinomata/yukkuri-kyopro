import sys


def build(s: int):
    """面積 S/2 で、単位正方形をちょうど 1 つ含む三角形。なければ None"""
    if s in (1, 2, 3, 5, 7):
        return None  # 小さい S は作れない（全探索で確かめられている）
    if s == 4:
        return (1, 1, 1, 3, 3, 3)
    # p + q + 1 = S となる互いに素な p, q ≥ 2 を選ぶ
    t = s - 1
    if t % 2 == 1:
        p, q = 2, t - 2  # q は奇数なので 2 と互いに素
    elif (t // 2) % 2 == 0:
        p, q = t // 2 - 1, t // 2 + 1  # 差 2 の奇数どうし → 互いに素
    else:
        p, q = t // 2 - 2, t // 2 + 2  # 差 4 の奇数どうし → 互いに素
    # s' q - t' p = 1 となる 1 ≤ s' < p, 1 ≤ t' < q（s' は q の mod p での逆元）
    sp = pow(q, -1, p)
    tp = (sp * q - 1) // p
    # 三角形 (0,0), (p,q), (s'+1, t'-1)：面積は (p + q + 1) / 2 = S / 2
    return (0, 0, p, q, sp + 1, tp - 1)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    out = []
    for i in range(int(data[0])):
        tri = build(int(data[1 + i]))
        if tri is None:
            out.append("No")
        else:
            out.append("Yes")
            out.append(" ".join(map(str, tri)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
