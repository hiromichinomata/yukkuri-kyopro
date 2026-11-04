import sys

MOD = 998244353


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    e = n * (n - 1) // 2
    c = [[0] * (e + 1) for _ in range(e + 1)]  # 二項係数
    for i in range(e + 1):
        c[i][0] = 1
        for j in range(1, i + 1):
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD
    # トーナメントの強連結成分は一列に並ぶので、「すべての辺が A から B へ向く」ような分割 (A, B)
    # （A は空でない）の数が、ちょうど強連結成分の数になる。そこで (A, B) とトーナメントの組を数える。
    # 頂点を番号順に A か B へ振り分ける。B に入れた頂点は、それまでの A の頂点すべてから
    # 「小さい番号 → 大きい番号」の辺を受ける（A に入れた頂点は逆向きの辺になる）。
    # dp[a][x]: A に a 個入れて、A→B の辺のうち小→大のものが x 本
    dp = [[0] * (e + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):  # i 個振り分け済み
        ndp = [[0] * (e + 1) for _ in range(n + 1)]
        for a in range(i + 1):
            row = dp[a]
            for x in range(e + 1):
                v = row[x]
                if v:
                    ndp[a + 1][x] = (ndp[a + 1][x] + v) % MOD  # A へ
                    if x + a <= e:
                        ndp[a][x + a] = (ndp[a][x + a] + v) % MOD  # B へ（小→大の辺が a 本増える）
        dp = ndp
    ans = 0
    for a in range(1, n + 1):
        inner = a * (a - 1) // 2 + (n - a) * (n - a - 1) // 2  # A・B の内側の辺は向きが自由
        for x in range(e + 1):
            if dp[a][x] and 0 <= m - x <= inner:
                ans = (ans + dp[a][x] * c[inner][m - x]) % MOD
    print(ans)


if __name__ == "__main__":
    main()
