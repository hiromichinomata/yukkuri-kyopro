import sys


def prime_factors(n: int) -> list:
    res = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            res.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        res.append(n)
    return res


def primitive_root(p: int) -> int:
    """素数 p の最小の原根 g を返す。
    g が原根 ⇔ p-1 のすべての素因数 q について g^((p-1)/q) ≠ 1 (mod p)"""
    if p == 2:
        return 1
    qs = prime_factors(p - 1)
    g = 2
    while True:
        if all(pow(g, (p - 1) // q, p) != 1 for q in qs):
            return g
        g += 1


def main() -> None:
    p = int(sys.stdin.readline())
    print(primitive_root(p))


if __name__ == "__main__":
    main()
