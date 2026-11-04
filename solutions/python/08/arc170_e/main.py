import sys

MOD = 998244353


def solve(n: int, p100: int) -> int:
    p = p100 * pow(100, MOD - 2, MOD) % MOD
    c = (2 * p - 1) % MOD  # 1 歩で「同じ向きが続く確率 − 向きが変わる確率」
    m = (n - 1) % MOD  # 文字列の長さ N-1（mod で使う）
    # 処理は「長さ N-1 の L / R の列（先頭は L、同じ文字が続く確率 p、変わる確率 1-p）」と対応し、
    # D の和は l(l+1)/2 + r(r+1)/2（l, r は L, R の個数）。
    # これは「同じ文字の組 (i ≤ j) の数」なので、期待値の線形性で
    #   E = Σ_{i ≤ j} P(S_i = S_j) = Σ_{d=0}^{N-2} (N-1-d) (1 + c^d) / 2
    # Σ_{d=0}^{m-1} (m-d) c^d = (m - c(1 - c^m)/(1 - c)) / (1 - c) を使う
    inv1c = pow((1 - c) % MOD, MOD - 2, MOD)
    cm = pow(c, (n - 1) % (MOD - 1), MOD) if c else (1 if n - 1 == 0 else 0)
    geo = (m - c * (1 - cm) % MOD * inv1c) % MOD * inv1c % MOD
    tri = m * (m + 1) % MOD * pow(2, MOD - 2, MOD) % MOD
    return (tri + geo) * pow(2, MOD - 2, MOD) % MOD


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = [str(solve(int(data[1 + 2 * i]), int(data[2 + 2 * i]))) for i in range(t)]
    print("\n".join(out))


if __name__ == "__main__":
    main()
