import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = sorted(map(int, input().split()))  # ソートすると |a_i - a_j| = a_j - a_i（i < j）
    ans = 0
    prefix = 0  # a_0 + ... + a_(j-1)
    for j, x in enumerate(a):
        # a_j は「自分より前の j 個」との差で j 回足され、前の値の和が引かれる（主客転倒）
        ans += x * j - prefix
        prefix += x
    print(ans)


if __name__ == "__main__":
    main()
