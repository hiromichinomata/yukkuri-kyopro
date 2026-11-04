import sys
from math import gcd


def primes(k: int) -> list:
    """小さい順に k 個の素数"""
    res, x = [], 2
    while len(res) < k:
        if all(x % p for p in res if p * p <= x):
            res.append(x)
        x += 1
    return res


def main() -> None:
    n = int(sys.stdin.readline())
    if n == 2:
        print("4 7\n23 10")  # N = 2 は下の作り方だと値が重なるので、手で作った例（余りはすべて 3）
        return
    # 市松模様の「白」マス (i + j が偶数) に、2 方向の対角線ごとの素数の積を置く:
    #   右下がりの対角線 (i + j) / 2 に小さい素数、右上がりの対角線 (i - j + N) / 2 に次の素数
    # 「黒」マスには、隣の白マスの値の最小公倍数 + 1 を置く。すると隣り合う 2 つは必ず
    # 「大きい方 mod 小さい方 = 1」になる（m = 1）。最小公倍数は素数 4 個の積で 10^15 以下に収まる
    k = n + 2
    ps = primes(2 * k)
    p1, p2 = ps[:k], ps[k:]
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                a[i][j] = p1[(i + j) // 2] * p2[(i - j + n) // 2]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                l = 1
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    x, y = i + di, j + dj
                    if 0 <= x < n and 0 <= y < n:
                        l = l // gcd(l, a[x][y]) * a[x][y]
                a[i][j] = l + 1
    print("\n".join(" ".join(map(str, row)) for row in a))


if __name__ == "__main__":
    main()
