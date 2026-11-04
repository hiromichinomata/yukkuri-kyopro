import itertools
import math
import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n)]
    total = 0.0
    count = 0
    for order in itertools.permutations(range(n)):  # N! 通り（N ≤ 8 なので 40320 通り）
        for i in range(n - 1):
            (x1, y1), (x2, y2) = pts[order[i]], pts[order[i + 1]]
            total += math.hypot(x1 - x2, y1 - y2)
        count += 1
    print(f"{total / count:.10f}")


if __name__ == "__main__":
    main()
