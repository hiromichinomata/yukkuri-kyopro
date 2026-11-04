import sys

MOD = 998244353


def main() -> None:
    n, m, a, b = map(int, sys.stdin.readline().split())
    # 勝てる配置では、黒石は「縦 → 横 → 縦 → …」（または横から）と交互に動いて元の位置に戻る。
    # 白石は「隣り合う 2 行の組」K 個と「隣り合う 2 列の組」K 個に並び（M = 2K）、
    # 組を訪れる順番を決めると配置が 1 つに決まる。最後に訪れる組は黒石の行（列）を含み、
    # その直前の組は、黒石が戻ってくる側（着地する向きの手前側）になければならない
    if m % 2 or m < 4:
        print(0)
        return
    k = m // 2
    fac = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % MOD
    inv = [1] * (n + 1)
    inv[n] = pow(fac[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        inv[i - 1] = inv[i] * i % MOD

    def comb(x, y):
        if y < 0 or x < y or x < 0:
            return 0
        return fac[x] * inv[y] % MOD * inv[x - y] % MOD

    def side_sum(l, r, j):
        """長さ l（直前の組が来る側）と長さ r の 2 区間から、隣り合う 2 マスの組を合計 j 個選ぶ方法を
        「l 側の組の数」で重みづけして足す（直前の組を l 側から 1 つ選ぶ分）"""
        s = 0
        for i in range(1, j + 1):
            s += i * comb(l - i, i) % MOD * comb(r - (j - i), j - i)
        return s % MOD

    def count_line(x):
        """行（または列）方向の数え方。最後の組が x を含む 2 通りを足し、残りの並べ方 (K-2)! を掛ける"""
        tot = 0
        if x - 1 >= 1:  # 組 {x-1, x}: 小さい側から来て x に着地 → 直前の組は 1..x-2 にある
            tot += side_sum(x - 2, n - x, k - 1)
        if x + 1 <= n:  # 組 {x, x+1}: 大きい側から来る → 直前の組は x+2..n にある
            tot += side_sum(n - x - 1, x - 1, k - 1)
        return tot % MOD * fac[k - 2] % MOD

    # 縦から始めるか横から始めるかで 2 倍
    print(2 * count_line(a) * count_line(b) % MOD)


if __name__ == "__main__":
    main()
