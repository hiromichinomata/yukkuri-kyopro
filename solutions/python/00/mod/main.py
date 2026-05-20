MOD = 998244353


def add_mod(a: int, b: int, mod: int = MOD) -> int:
    return (a + b) % mod


def mul_mod(a: int, b: int, mod: int = MOD) -> int:
    return (a * b) % mod


def main() -> None:
    print(add_mod(10**9, 10**9))
    print(mul_mod(10**5, 10**5))


if __name__ == "__main__":
    main()
