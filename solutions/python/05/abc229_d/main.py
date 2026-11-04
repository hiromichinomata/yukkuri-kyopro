import sys


def main() -> None:
    input = sys.stdin.readline
    s = input().strip()
    k = int(input())
    ans = left = dots = 0
    for right, ch in enumerate(s):  # 尺取り法: 区間 [left, right] の「.」を K 個以下に保つ
        if ch == ".":
            dots += 1
        while dots > k:
            if s[left] == ".":
                dots -= 1
            left += 1
        ans = max(ans, right - left + 1)
    print(ans)


if __name__ == "__main__":
    main()
