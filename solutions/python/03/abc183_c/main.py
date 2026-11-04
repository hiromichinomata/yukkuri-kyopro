import itertools
import sys


def main() -> None:
    input = sys.stdin.readline
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for order in itertools.permutations(range(1, n)):  # 都市 1 は始点・終点に固定
        route = (0,) + order + (0,)
        if sum(t[route[i]][route[i + 1]] for i in range(n)) == k:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
