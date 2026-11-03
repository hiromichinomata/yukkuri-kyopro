import sys
from collections import Counter


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    # 区間 (l, r] の和が 0 ⇔ 累積和 S[l] == S[r]
    cnt = Counter([0])  # S[0] = 0
    s = 0
    ans = 0
    for x in a:
        s += x
        ans += cnt[s]  # これまでに同じ累積和が出た回数だけ、和 0 の区間が増える
        cnt[s] += 1
    print(ans)


if __name__ == "__main__":
    main()
