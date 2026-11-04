import sys

MOD = 10**9 + 7


def main() -> None:
    n = int(sys.stdin.readline())
    m = n - 1  # 機械の数
    fac = [1] * (m + 1)
    for i in range(1, m + 1):
        fac[i] = fac[i - 1] * i % MOD
    inv = [1] * (m + 1)
    inv[m] = pow(fac[m], MOD - 2, MOD)
    for i in range(m, 0, -1):
        inv[i - 1] = inv[i] * i % MOD

    def comb(a, b):
        if b < 0 or b > a or a < 0:
            return 0
        return fac[a] * inv[b] % MOD * inv[a - b] % MOD

    # f[k]: 最初の k 台で全部塗り終わっている順列の数。
    # k 台で全マスを塗る ⇔ 機械 1 と機械 N-1 を含み、使わない機械が 2 台続かない。
    # 使わない m-k 台を、使う k 台の間の k-1 か所に 1 台ずつ入れる → C(k-1, m-k) 通り
    f = [0] * (m + 1)
    for k in range(1, m + 1):
        f[k] = comb(k - 1, m - k) * fac[k] % MOD * fac[m - k] % MOD
    # ちょうど k 台目で塗り終わる順列は f[k] - f[k-1] 個。スコア k を掛けて足す
    ans = 0
    for k in range(1, m + 1):
        ans = (ans + k * (f[k] - f[k - 1])) % MOD
    print(ans)


if __name__ == "__main__":
    main()
