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
    dp = [[0] * (m + 2) for _ in range(m + 2)]
    dp[0][0] = 1
    for v in range(m, 0, -1):
        if kind[v] == 2:
            continue
        ndp = [[0] * (m + 2) for _ in range(m + 2)]
        for j in range(m + 1):
            for k in range(m + 1):
                x = dp[j][k]
                if not x:
                    continue
                if kind[v] == 0:
                    ndp[j + 1][k] = (ndp[j + 1][k] + x) % MOD  # 自分より小さい値を待つ
                    if j:
                        ndp[j - 1][k] = (ndp[j - 1][k] + x) % MOD  # 待っている自由な値と組んで B = v
                    if k:
                        ndp[j][k - 1] = (ndp[j][k - 1] + x * k) % MOD  # 片方決まった組の空きに入る（どの組か k 通り）
                else:
                    ndp[j][k + 1] = (ndp[j][k + 1] + x) % MOD  # 小さい値が空きに入るのを待つ
                    if j:
                        ndp[j - 1][k] = (ndp[j - 1][k] + x) % MOD  # 待っている自由な値が空きに入り B = v
        dp = ndp
    ans = dp[0][0]
    for i in range(1, c + 1):
        ans = ans * i % MOD
    print(ans)


if __name__ == "__main__":
    main()
