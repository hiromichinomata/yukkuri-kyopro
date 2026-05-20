MOD = 10**9 + 7


def mat_mul(A, B, mod=MOD):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if A[i][k] == 0:
                continue
            for j in range(p):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C


def mat_pow(M, e, mod=MOD):
    n = len(M)
    res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while e:
        if e & 1:
            res = mat_mul(res, M, mod)
        M = mat_mul(M, M, mod)
        e >>= 1
    return res


def fib(n, mod=MOD):
    if n == 0:
        return 0
    T = [[1, 1], [1, 0]]
    Tn = mat_pow(T, n - 1, mod)
    return Tn[0][0]


def main() -> None:
    for n in range(10):
        print(fib(n), end=" ")
    print()


if __name__ == "__main__":
    main()
