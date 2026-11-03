import sys


def ext_gcd(a: int, b: int) -> tuple:
    """a*x + b*y = g = gcd(a, b) となる (g, x, y) を返す"""
    if b == 0:
        return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y


def crt(rs: list, ms: list) -> tuple:
    """x ≡ rs[i] (mod ms[i]) をすべて満たす x を (x, lcm) で返す。解なしなら (0, -1)。
    法どうしが互いに素でなくてもよい"""
    r0, m0 = 0, 1
    for r1, m1 in zip(rs, ms):
        r1 %= m1
        # x = r0 + m0 * t として、m0 * t ≡ r1 - r0 (mod m1) を解く
        g, p, _ = ext_gcd(m0, m1)
        if (r1 - r0) % g != 0:
            return 0, -1  # 矛盾（解なし）
        t = (r1 - r0) // g * p % (m1 // g)
        r0 += m0 * t
        m0 = m0 // g * m1
        r0 %= m0
    return r0, m0


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    rs, ms = [], []
    for _ in range(n):
        r, m = map(int, input().split())
        rs.append(r)
        ms.append(m)
    x, lcm = crt(rs, ms)
    print(-1 if lcm == -1 else f"{x} {lcm}")


if __name__ == "__main__":
    main()
