import sys


def main() -> None:
    grid = [
        list("..#."),
        list(".#.."),
        list("...."),
    ]
    h, w = len(grid), len(grid[0])
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    si, sj = 1, 0
    ok = []
    for k in range(4):
        ni, nj = si + di[k], sj + dj[k]
        if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] != "#":
            ok.append((ni, nj))
    print(ok)


if __name__ == "__main__":
    main()
