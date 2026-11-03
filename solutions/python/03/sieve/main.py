import sys


def sieve(n: int) -> list:
    """is_p[i] が True なら i は素数（0 <= i <= n）"""
    is_p = [True] * (n + 1)
    is_p[0] = False
    if n >= 1:
        is_p[1] = False
    i = 2
    while i * i <= n:
        if is_p[i]:
            for j in range(i * i, n + 1, i):  # i*i 未満は小さい素数で消し済み
                is_p[j] = False
        i += 1
    return is_p


def main() -> None:
    n = int(sys.stdin.readline())
    is_p = sieve(n)
    primes = [i for i in range(n + 1) if is_p[i]]
    print(len(primes))
    print(*primes)


if __name__ == "__main__":
    main()
