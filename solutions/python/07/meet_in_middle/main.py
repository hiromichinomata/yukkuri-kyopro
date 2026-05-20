import bisect


def subset_sums(xs):
    sums = [0]
    for x in xs:
        sums = [s + x for s in sums] + sums
    return sums


def can_make_sum(xs, target):
    n = len(xs)
    mid = n // 2
    left = sorted(subset_sums(xs[:mid]))
    right = subset_sums(xs[mid:])
    for s in right:
        need = target - s
        i = bisect.bisect_left(left, need)
        if i < len(left) and left[i] == need:
            return True
    return False


def main() -> None:
    xs = [1, 2, 4, 8, 16]
    for t in [0, 7, 15, 31, 32]:
        print(t, can_make_sum(xs, t))


if __name__ == "__main__":
    main()
