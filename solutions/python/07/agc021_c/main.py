import sys


def fill(n, m, a, b, pinwheel):
    """敷き詰めを試す。成功すれば盤面（文字のリストのリスト）、失敗すれば None"""
    g = [["."] * m for _ in range(n)]
    block_rows = n - n % 2  # 2×2 ブロックに分ける部分は偶数 × 偶数
    block_cols = m - m % 2
    skip = None
    if pinwheel:
        # 右下 3×3 に「風車」型で 1×2 を 2 枚、2×1 を 2 枚置く（中央は空き）
        r, c = n - 3, m - 3
        for (i, j), ch in {(0, 0): "<", (0, 1): ">", (0, 2): "^", (1, 2): "v", (2, 1): "<", (2, 2): ">",
                           (1, 0): "^", (2, 0): "v"}.items():
            g[r + i][c + j] = ch
        a -= 2
        b -= 2
        skip = (n - 3, m - 3)  # 風車と重なる 2×2 ブロック（左上の座標）
    # 最後の行（N が奇数）: 1×2 を左から置く。2×1 は入らない
    if n % 2:
        for j in range(0, m - 1, 2):
            if a > 0 and g[n - 1][j] == "." and g[n - 1][j + 1] == ".":
                g[n - 1][j], g[n - 1][j + 1] = "<", ">"
                a -= 1
    # 最後の列（M が奇数）: 2×1 を上から置く
    if m % 2:
        for i in range(0, n - 1, 2):
            if b > 0 and g[i][m - 1] == "." and g[i + 1][m - 1] == ".":
                g[i][m - 1], g[i + 1][m - 1] = "^", "v"
                b -= 1
    # 残りの 2×2 ブロック: 1×2 なら 2 枚、2×1 でも 2 枚入る（1 枚だけでもよい）
    for i in range(0, block_rows, 2):
        for j in range(0, block_cols, 2):
            if (i, j) == skip:
                continue
            if a > 0:
                g[i][j], g[i][j + 1] = "<", ">"
                a -= 1
                if a > 0:
                    g[i + 1][j], g[i + 1][j + 1] = "<", ">"
                    a -= 1
            elif b > 0:
                g[i][j], g[i + 1][j] = "^", "v"
                b -= 1
                if b > 0:
                    g[i][j + 1], g[i + 1][j + 1] = "^", "v"
                    b -= 1
    return g if a <= 0 and b <= 0 and a == 0 and b == 0 else None


def main() -> None:
    n, m, a, b = map(int, sys.stdin.readline().split())
    tries = [False]
    if n % 2 and m % 2 and n >= 3 and m >= 3 and a >= 2 and b >= 2:
        tries.append(True)  # 両方奇数のときは、風車を使うと 1 マス分得をすることがある
    for pinwheel in tries:
        g = fill(n, m, a, b, pinwheel)
        if g is not None:
            print("YES")
            print("\n".join("".join(row) for row in g))
            return
    print("NO")


if __name__ == "__main__":
    main()
