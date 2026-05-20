def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def main() -> None:
    print(ccw((0, 0), (1, 0), (0, 1)))


if __name__ == "__main__":
    main()
