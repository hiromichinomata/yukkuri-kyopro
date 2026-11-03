import sys


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    color = [-1] * n
    ans = 1
    for s in range(n):
        if color[s] != -1:
            continue
        # 連結成分の頂点を DFS 順に並べる（どの頂点も、先に並んだ頂点のどれかと隣り合う）
        order, stack = [], [s]
        color[s] = 0
        while stack:
            v = stack.pop()
            order.append(v)
            for to in g[v]:
                if color[to] == -1:
                    color[to] = 0
                    stack.append(to)
        for v in order:
            color[v] = -1

        def count(i):
            if i == len(order):
                return 1
            v = order[i]
            total = 0
            for c in range(3):
                if all(color[to] != c for to in g[v]):
                    color[v] = c
                    total += count(i + 1)
                    color[v] = -1
            return total

        # 先頭の頂点の色は 3 通りとも対称なので、0 に固定して 3 倍する
        color[order[0]] = 0
        ways = count(1) * 3
        for v in order:
            color[v] = 3  # 塗り終わった成分は「どの色とも違う」扱いにしておく
        ans *= ways
    print(ans)


if __name__ == "__main__":
    main()
