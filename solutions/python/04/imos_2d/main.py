import sys


def main() -> None:
    input = sys.stdin.readline
    h, w, n = map(int, input().split())
    # 差分は 1 マス大きく取る（右端・下端の +1 が溢れないように）
    d = [[0] * (w + 1) for _ in range(h + 1)]
    for _ in range(n):
        # 矩形 [r1, r2) × [c1, c2) に +1（0-indexed、右端・下端は含まない）
        r1, c1, r2, c2 = map(int, input().split())
        d[r1][c1] += 1
        d[r1][c2] -= 1
        d[r2][c1] -= 1
        d[r2][c2] += 1
    # 横方向に累積 → 縦方向に累積
    for i in range(h + 1):
        for j in range(1, w + 1):
            d[i][j] += d[i][j - 1]
    for i in range(1, h + 1):
        for j in range(w + 1):
            d[i][j] += d[i - 1][j]
    for i in range(h):
        print(*d[i][:w])


if __name__ == "__main__":
    main()
