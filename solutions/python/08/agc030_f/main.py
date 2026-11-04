import sys

MOD = 10**9 + 7


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = [int(x) for x in data[1 : 1 + 2 * n]]
    m = 2 * n
    # 組 (A_{2i-1}, A_{2i}) を 3 種類に分ける:
    #   両方決まっている → B は決まっているので無視 / 片方だけ決まっている / 両方 -1（c 組）
    kind = [0] * (m + 1)  # 0: A に出てこない値、1: 片方だけ決まった組の値、2: 両方決まった組の値
    c = 0
    for i in range(n):
        x, y = a[2 * i], a[2 * i + 1]
        if x != -1 and y != -1:
            kind[x] = kind[y] = 2
        elif x == -1 and y == -1:
            c += 1
        else:
            kind[max(x, y)] = 1
    # 値の大きい方から見ていき、「まだ相手の決まっていない値」の数を持つ DP:
    #   j: A に出てこない値で、相手待ちのもの  k: 片方だけ決まった組の値で、相手待ちのもの
    # 両方 -1 の組どうしの区別（どの組に入るか）は最後に c! を掛けてつける
    # j は「処理した A に出てこない値」の数、k は「処理した片方だけ決まった組の値」の数を超えない。
    # どちらも、まだ処理していない（小さい）値で埋めるので j + k ≤ 残りの値の数。表はこの範囲だけ持つ
    vals = [v for v in range(m, 0, -1) if kind[v] != 2]
    dp = [[1]]  # dp[j][k]
    c0 = c1 = 0
    for idx, v in enumerate(vals):
        rest = len(vals) - idx - 1  # v より小さい、まだ処理していない値の数
        old, ow = dp, len(dp[0])
        if kind[v] == 0:
            c0 += 1
        else:
            c1 += 1
        nj, nk = min(c0, rest) + 1, min(c1, rest) + 1
        z = [0] * (nk + 1)
        pad = [r + [0] * (nk + 1 - ow) for r in old] + [z, z]  # 範囲外を 0 として読めるように広げる
        dp = []
        for j in range(nj):
            up, cur = pad[j + 1], pad[j]
            down = pad[j - 1] if j else z
            w = min(nk, rest - j + 1)
            if w <= 0:
                dp.append([0] * nk)
                continue
            if kind[v] == 0:
                # 自分より小さい値を待つ（j-1 → j）／待っている自由な値と組む（j+1 → j）／
                # 片方決まった組の空きに入る（k+1 → k、どの組か k+1 通り）
                row = [(down[k] + up[k] + cur[k + 1] * (k + 1)) % MOD for k in range(w)]
            else:
                # 小さい値が空きに入るのを待つ（k-1 → k）／待っている自由な値が空きに入る（j+1 → j）
                row = [((cur[k - 1] if k else 0) + up[k]) % MOD for k in range(w)]
            dp.append(row + [0] * (nk - w))
    ans = dp[0][0]
    for i in range(1, c + 1):
        ans = ans * i % MOD
    print(ans)


if __name__ == "__main__":
    main()
