import sys


def main() -> None:
    input = sys.stdin.readline
    n, m, x = map(int, input().split())
    books = [list(map(int, input().split())) for _ in range(n)]
    INF = 10**18
    best = INF
    for mask in range(1 << n):  # どの本を買うかを 2^N 通り全部試す
        cost = 0
        level = [0] * m
        for i in range(n):
            if mask >> i & 1:
                cost += books[i][0]
                for j in range(m):
                    level[j] += books[i][j + 1]
        if all(v >= x for v in level):
            best = min(best, cost)
    print(best if best < INF else -1)


if __name__ == "__main__":
    main()
