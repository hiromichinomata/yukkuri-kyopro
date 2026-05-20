import bisect


def lower_bound(a: list, x: int) -> int:
    ng, ok = -1, len(a)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if a[mid] >= x:
            ok = mid
        else:
            ng = mid
    return ok


def main() -> None:
    a = [1, 3, 3, 5, 7]
    print(bisect.bisect_left(a, 4))
    print(lower_bound(a, 4))


if __name__ == "__main__":
    main()
