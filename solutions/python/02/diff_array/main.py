def main() -> None:
    n = 5
    diff = [0] * (n + 2)

    def add_range(l: int, r: int, v: int) -> None:
        diff[l] += v
        diff[r + 1] -= v

    add_range(1, 3, 10)
    add_range(2, 5, 5)

    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = a[i - 1] + diff[i]
    print(a[1:])


if __name__ == "__main__":
    main()
