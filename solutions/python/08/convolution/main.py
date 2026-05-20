MOD = 998244353
G = 3


def ntt(a, invert=False):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        w = pow(G, (MOD - 1) // length, MOD)
        if invert:
            w = pow(w, MOD - 2, MOD)
        for i in range(0, n, length):
            wn = 1
            for k in range(length // 2):
                u = a[i + k]
                v = a[i + k + length // 2] * wn % MOD
                a[i + k] = (u + v) % MOD
                a[i + k + length // 2] = (u - v) % MOD
                wn = wn * w % MOD
        length <<= 1
    if invert:
        inv_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = a[i] * inv_n % MOD


def conv(a, b):
    need = 1
    while need < len(a) + len(b) - 1:
        need <<= 1
    fa = a[:] + [0] * (need - len(a))
    fb = b[:] + [0] * (need - len(b))
    ntt(fa)
    ntt(fb)
    fa = [fa[i] * fb[i] % MOD for i in range(need)]
    ntt(fa, invert=True)
    return fa[: len(a) + len(b) - 1]


def main() -> None:
    a = [1, 2, 3]
    b = [4, 5]
    print(conv(a, b))


if __name__ == "__main__":
    main()
