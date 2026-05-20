MOD = 10**9 + 7


def gauss(A, mod=MOD):
    n = len(A)
    m = len(A[0])
    row = 0
    for col in range(m - 1):
        pivot = -1
        for r in range(row, n):
            if A[r][col] % mod:
                pivot = r
                break
        if pivot == -1:
            continue
        A[row], A[pivot] = A[pivot], A[row]
        inv = pow(A[row][col], mod - 2, mod)
        for c in range(col, m):
            A[row][c] = A[row][c] * inv % mod
        for r in range(n):
            if r == row:
                continue
            factor = A[r][col]
            if factor == 0:
                continue
            for c in range(col, m):
                A[r][c] = (A[r][c] - factor * A[row][c]) % mod
        row += 1
    return A


def main() -> None:
    A = [
        [2, 1, 5],
        [1, 1, 3],
    ]
    print(gauss([row[:] for row in A]))


if __name__ == "__main__":
    main()
