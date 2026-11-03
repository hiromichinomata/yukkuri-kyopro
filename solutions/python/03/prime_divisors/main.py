import sys


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:  # √n まで割ってみれば十分
        if n % i == 0:
            return False
        i += 1
    return True


def divisors(n: int) -> list:
    small, large = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i != n // i:  # 平方数で同じ約数を 2 回入れない
                large.append(n // i)
        i += 1
    return small + large[::-1]  # 昇順


def factorize(n: int) -> list:
    res = []  # (素因数, 指数)
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            res.append((p, e))
        p += 1
    if n > 1:  # 残りは √n より大きい素数
        res.append((n, 1))
    return res


def main() -> None:
    n = int(sys.stdin.readline())
    print("Yes" if is_prime(n) else "No")
    print(*divisors(n))
    print(*(f"{p}^{e}" for p, e in factorize(n)))


if __name__ == "__main__":
    main()
