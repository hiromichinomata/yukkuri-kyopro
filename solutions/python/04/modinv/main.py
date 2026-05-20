MOD = 998244353


def mod_pow(a, e, mod=MOD):
    res = 1
    while e:
        if e & 1:
            res = res * a % mod
        a = a * a % mod
        e >>= 1
    return res


def prepare_fac(n, mod=MOD):
    fac = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % mod
    inv[n] = mod_pow(fac[n], mod - 2, mod)
    for i in range(n, 0, -1):
        inv[i - 1] = inv[i] * i % mod
    return fac, inv


def ncr(n, r, fac, inv, mod=MOD):
    if r < 0 or r > n:
        return 0
    return fac[n] * inv[r] % mod * inv[n - r] % mod


def main() -> None:
    fac, inv = prepare_fac(10)
    print(ncr(5, 2, fac, inv))


if __name__ == "__main__":
    main()
