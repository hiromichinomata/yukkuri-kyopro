import sys

MOD = 10**9 + 7


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    m = 2 * n
    pair = [-1] * m
    for i in range(k):
        a, b = int(data[2 + 2 * i]) - 1, int(data[3 + 2 * i]) - 1
        pair[a], pair[b] = b, a
    # g[x]: 自由な点 x 個を 2 つずつ組にする方法の数（x が奇数なら 0）
    g = [0] * (m + 1)
    g[0] = 1
    for x in range(2, m + 1, 2):
        g[x] = g[x - 2] * (x - 1) % MOD
    # free[i]: 点 0〜i-1 のうち、まだ組の決まっていない点の数（累積和）
    free = [0] * (m + 1)
    for i in range(m):
        free[i + 1] = free[i] + (pair[i] == -1)
    # 連結成分を「その成分の一番左の点 l と一番右の点 r」で数える（主客転倒）。
    # dp[l][r]: 区間 [l, r] の点どうしだけで組み、l と r が同じ成分になる方法の数
    #   = （区間内だけで組む方法）−（l を含む成分が m で終わり、(m, r] は別に組む方法）
    dp = [[0] * m for _ in range(m)]
    ans = 0
    total_free = free[m]
    for l in range(m):
        row = dp[l]
        lo, hi = m, -1  # 区間 [l, r] の点の組の相手の最小・最大（決まっているものだけ）
        for r in range(l, m):
            if pair[r] != -1:
                lo, hi = min(lo, pair[r]), max(hi, pair[r])
            if (r - l) % 2 == 0 or lo < l or hi > r:
                continue  # 点が奇数個、または決まっている組が区間をまたいでいる
            v = g[free[r + 1] - free[l]]
            for mid in range(l + 1, r, 2):
                if row[mid]:
                    v -= row[mid] * g[free[r + 1] - free[mid + 1]]
            v %= MOD
            row[r] = v
            # 区間の外の点は外どうしで自由に組む
            ans = (ans + v * g[total_free - (free[r + 1] - free[l])]) % MOD
    print(ans)


if __name__ == "__main__":
    main()
