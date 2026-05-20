def build_2d(a):
    h, w = len(a), len(a[0])
    s = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i - 1][j - 1]
    return s


def rect_sum(s, h1, w1, h2, w2):
    return s[h2][w2] - s[h1 - 1][w2] - s[h2][w1 - 1] + s[h1 - 1][w1 - 1]


def main() -> None:
    a = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    s = build_2d(a)
    print(rect_sum(s, 1, 1, 2, 2))


if __name__ == "__main__":
    main()
