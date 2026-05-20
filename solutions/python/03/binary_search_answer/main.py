import sys


def main() -> None:
    n = int(sys.stdin.readline())

    def check(x: int) -> bool:
        return x * x <= n

    hi = 1
    while check(hi):
        hi *= 2
    lo, hi_ans = 0, hi
    while lo < hi_ans:
        mid = (lo + hi_ans + 1) // 2
        if check(mid):
            lo = mid
        else:
            hi_ans = mid - 1
    print(lo)


if __name__ == "__main__":
    main()
