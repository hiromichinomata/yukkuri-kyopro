import sys

BEATS = {("G", "C"), ("C", "P"), ("P", "G")}  # (勝つ手, 負ける手)


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    hands = [input().strip() for _ in range(2 * n)]
    wins = [0] * (2 * n)
    rank = list(range(2 * n))  # 順位順の選手番号（0 始まり）
    for j in range(m):
        for k in range(n):
            x, y = rank[2 * k], rank[2 * k + 1]
            if (hands[x][j], hands[y][j]) in BEATS:
                wins[x] += 1
            elif (hands[y][j], hands[x][j]) in BEATS:
                wins[y] += 1
        rank.sort(key=lambda i: (-wins[i], i))  # 勝ち数の多い順、同じなら番号の小さい順
    print("\n".join(str(i + 1) for i in rank))


if __name__ == "__main__":
    main()
