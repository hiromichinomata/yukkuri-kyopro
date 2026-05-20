import bisect


def main() -> None:
    values = [10**9, 5, 10**9, 7, 5]
    uniq = sorted(set(values))
    compressed = [bisect.bisect_left(uniq, v) for v in values]
    print(uniq)
    print(compressed)


if __name__ == "__main__":
    main()
