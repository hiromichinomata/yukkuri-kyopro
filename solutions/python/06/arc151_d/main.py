import sys

MOD = 998244353


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    a = [int(x) for x in data[2 : 2 + (1 << n)]]
    # 1 回の操作は、ビット X が違うだけの 2 つ組 (A_0側, A_1側) に 2×2 行列を掛けることと同じ:
    #   Y = 0: (a0, a1) → (a0, a1 + a0)、 Y = 1: (a0, a1) → (a0 + a1, a1)
    # 違うビットの操作どうしは順番を入れ替えても結果が同じなので、ビットごとに行列をまとめて掛ける
    mats = [[1, 0, 0, 1] for _ in range(n)]  # [[p, q], [r, s]] を (p, q, r, s) で持つ（単位行列から）
    pos = 2 + (1 << n)
    for i in range(q):
        x, y = int(data[pos + 2 * i]), int(data[pos + 2 * i + 1])
        p, qq, r, s = mats[x]
        if y == 0:  # 下の行に上の行を足す
            mats[x] = [p, qq, (r + p) % MOD, (s + qq) % MOD]
        else:  # 上の行に下の行を足す
            mats[x] = [(p + r) % MOD, (qq + s) % MOD, r, s]
    for x in range(n):
        p, qq, r, s = mats[x]
        if (p, qq, r, s) == (1, 0, 0, 1):
            continue
        step = 1 << x
        for base in range(0, 1 << n, step << 1):
            for j in range(base, base + step):
                a0, a1 = a[j], a[j + step]
                a[j] = (p * a0 + qq * a1) % MOD
                a[j + step] = (r * a0 + s * a1) % MOD
    print(*a)


if __name__ == "__main__":
    main()
