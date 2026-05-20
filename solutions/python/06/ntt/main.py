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
            for j in range(length // 2):
                u = a[i + j]
                v = a[i + j + length // 2] * w % MOD
                a[i + j] = (u + v) % MOD
                a[i + j + length // 2] = (u - v) % MOD
        length <<= 1
    if invert:
        inv_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = a[i] * inv_n % MOD
    return a


def convolution(a, b):
    n1, n2 = len(a), len(b)
    n = 1
    while n < n1 + n2 - 1:
        n <<= 1
    fa = a + [0] * (n - n1)
    fb = b + [0] * (n - n2)
    fa = ntt(fa)
    fb = ntt(fb)
    for i in range(n):
        fa[i] = fa[i] * fb[i] % MOD
    return ntt(fa, invert=True)[: n1 + n2 - 1]


def main() -> None:
    print(convolution([1, 1], [1, 1]))
    print(convolution([1, 2, 3], [4, 5])[:6])


if __name__ == "__main__":
    main()
