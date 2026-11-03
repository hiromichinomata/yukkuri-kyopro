from collections import Counter


def main() -> None:
    xs = [1, 2, 2, 3, 3, 3]
    cnt = Counter(xs)
    print(cnt[2])
    for value, c in cnt.most_common(2):  # 多い順に (値, 個数)
        print(value, c)


if __name__ == "__main__":
    main()
