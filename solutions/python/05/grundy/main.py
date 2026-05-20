def nim_winner(piles: list) -> str:
    x = 0
    for p in piles:
        x ^= p
    return "first" if x else "second"


def mex(s: set) -> int:
    m = 0
    while m in s:
        m += 1
    return m


def main() -> None:
    print(nim_winner([1, 2, 3]))
    print(nim_winner([2, 2]))


if __name__ == "__main__":
    main()
