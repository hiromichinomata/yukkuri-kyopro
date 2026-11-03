import sys
from collections import deque


def main() -> None:
    input = sys.stdin.readline
    h, w = map(int, input().split())
    grid = "".join(input().strip() for _ in range(h))  # 1 次元にして i * w + j で表す
    warp = [[] for _ in range(26)]  # 文字ごとのテレポーター
    for idx, ch in enumerate(grid):
        if "a" <= ch <= "z":
            warp[ord(ch) - 97].append(idx)
    s, g = grid.index("S"), grid.index("G")
    dist = [-1] * (h * w)
    dist[s] = 0
    q = deque([s])
    used = [False] * 26
    while q:
        v = q.popleft()
        if v == g:
            break
        i, j = divmod(v, w)
        nbr = []
        if i > 0:
            nbr.append(v - w)
        if i < h - 1:
            nbr.append(v + w)
        if j > 0:
            nbr.append(v - 1)
        if j < w - 1:
            nbr.append(v + 1)
        ch = grid[v]
        if "a" <= ch <= "z" and not used[ord(ch) - 97]:
            # 同じ文字のテレポートは、最初に使ったときが一番早い → 一度使ったら二度と見ない
            used[ord(ch) - 97] = True
            nbr += warp[ord(ch) - 97]
        for to in nbr:
            if dist[to] == -1 and grid[to] != "#":
                dist[to] = dist[v] + 1
                q.append(to)
    print(dist[g])


if __name__ == "__main__":
    main()
