import bisect


def lis_length(a: list) -> int:
    tails = []
    for x in a:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def main() -> None:
    print(lis_length([3, 1, 4, 2, 5]))


if __name__ == "__main__":
    main()
