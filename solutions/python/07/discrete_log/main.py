def bsgs(a, b, p, m):
    a %= p
    b %= p
    step = int(m**0.5) + 1
    baby = {1: 0}
    cur = 1
    for j in range(1, step + 1):
        cur = cur * a % p
        if cur not in baby:
            baby[cur] = j
    factor = pow(a, step * (p - 2), p)
    gamma = b
    for i in range(step + 1):
        if gamma in baby:
            return i * step + baby[gamma]
        gamma = gamma * factor % p
    return -1


def main() -> None:
    p = 1_000_000_009
    a, b = 2, 8
    print(bsgs(a, b, p, p - 1))


if __name__ == "__main__":
    main()
