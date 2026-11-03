import sys


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    bulbs = []
    for _ in range(m):
        k, *s = map(int, input().split())
        bulbs.append([x - 1 for x in s])
    p = list(map(int, input().split()))
    ans = 0
    for mask in range(1 << n):  # スイッチの on / off を 2^N 通り全部試す
        if all(sum(mask >> s & 1 for s in bulbs[i]) % 2 == p[i] for i in range(m)):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
