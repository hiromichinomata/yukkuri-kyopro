def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def main() -> None:
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
