import sys
from collections import deque


def main() -> None:
    input = sys.stdin.readline
    h, w = map(int, input().split())
    grid = [input().strip() for _ in range(h)]
    si = sj = gi = gj = -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "S":
                si, sj = i, j
            if grid[i][j] == "G":
                gi, gj = i, j

    dist = [[-1] * w for _ in range(h)]
    dist[si][sj] = 0
    q = deque([(si, sj)])
    di = (-1, 1, 0, 0)
    dj = (0, 0, -1, 1)
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] != "#" and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    print(dist[gi][gj])


if __name__ == "__main__":
    main()
