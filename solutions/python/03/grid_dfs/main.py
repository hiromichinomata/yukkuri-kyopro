import sys

sys.setrecursionlimit(10**7)


def dfs(i: int, j: int, grid: list, seen: list) -> int:
    h, w = len(grid), len(grid[0])
    seen[i][j] = True
    size = 1
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and not seen[ni][nj] and grid[ni][nj] == ".":
            size += dfs(ni, nj, grid, seen)
    return size


def main() -> None:
    grid = ["..#.", ".#..", "...."]
    seen = [[False] * 4 for _ in range(3)]
    print(dfs(0, 0, grid, seen))


if __name__ == "__main__":
    main()
