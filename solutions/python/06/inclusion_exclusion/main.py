def count_coprime(n: int) -> int:
    """1..n のうち 2 でも 3 でも割り切れない個数（包除原理）"""
    primes = [2, 3]
    ans = n
    m = len(primes)
    for mask in range(1, 1 << m):
        bits = bin(mask).count("1")
        prod = 1
        for i in range(m):
            if mask >> i & 1:
                prod *= primes[i]
        if bits % 2:
            ans -= n // prod
        else:
            ans += n // prod
    return ans


def main() -> None:
    print(count_coprime(30))


if __name__ == "__main__":
    main()
