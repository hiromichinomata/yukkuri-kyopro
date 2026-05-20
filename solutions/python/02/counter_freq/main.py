from collections import Counter


def main() -> None:
    xs = [1, 2, 2, 3, 3, 3]
    cnt = Counter(xs)
    print(cnt[2])
    print(cnt.most_common(2))


if __name__ == "__main__":
    main()
