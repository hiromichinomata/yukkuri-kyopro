import sys

MOD = 998244353


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    p = [int(x) - 1 for x in input().split()]
    # 置換 P のサイクルの数 c を数える（i と P_i を Union-Find でつないだ連結成分の数と同じ）
    seen = [False] * n
    c = 0
    for i in range(n):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    # A = A∘P になるのは、サイクルごとに同じ値を入れる M^c 通り。
    # 残り M^N - M^c 通りは「A < A∘P」と「A > A∘P」に半分ずつ分かれる（対称性）
    print((pow(m, n, MOD) - pow(m, c, MOD)) * pow(2, MOD - 2, MOD) % MOD)


if __name__ == "__main__":
    main()
