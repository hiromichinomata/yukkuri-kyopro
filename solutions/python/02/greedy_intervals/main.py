import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort(key=lambda x: x[1])

    last = -10**18
    cnt = 0
    for l, r in intervals:
        if l >= last:
            cnt += 1
            last = r
    print(cnt)


if __name__ == "__main__":
    main()
