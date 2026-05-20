MOD = 998244353


def build_ncr(n: int, mod: int = MOD) -> list:
    c = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        c[i][0] = c[i][i] = 1
        for j in range(1, i):
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod
    return c


def main() -> None:
    c = build_ncr(10)
    print(c[5][2])


if __name__ == "__main__":
    main()
