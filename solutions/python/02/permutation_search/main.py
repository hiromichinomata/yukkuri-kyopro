import sys
from itertools import permutations


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    best = 10**18
    # 都市 0 から出発し、残りの都市を回る順番をすべて試す
    for order in permutations(range(1, n)):
        cost = 0
        cur = 0
        for nxt in order:
            cost += d[cur][nxt]
            cur = nxt
        cost += d[cur][0]  # 都市 0 に戻る
        best = min(best, cost)
    print(best)


if __name__ == "__main__":
    main()
