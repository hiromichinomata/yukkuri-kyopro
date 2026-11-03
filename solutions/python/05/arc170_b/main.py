import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    # 同じ値が 3 回出ると (x, x, x) が等差。値は 10 種類なので、長さ 21 の区間には
    # どれかの値が 3 回出て、必ず等差の 3 つ組がある（鳩の巣原理）。
    # よって「k で終わる 3 つ組 (i, j, k) の i の最大値」は k - 20 以上の範囲だけ見ればよい。
    W = 20
    ans = 0
    best = -1  # 右端が r 以下の 3 つ組のうち、左端 i の最大値（なければ -1）
    for k in range(n):
        for j in range(k - 1, max(-1, k - W - 1), -1):
            need = 2 * a[j] - a[k]  # a[i] - a[j] = a[j] - a[k] を満たす a[i]
            for i in range(j - 1, max(-1, k - W - 1), -1):
                if a[i] == need:
                    if i > best:
                        best = i
                    break  # この j では一番右の i だけ見れば十分
        # 右端が k の区間 [l, k] は、l <= best なら良い組
        ans += best + 1
    print(ans)


if __name__ == "__main__":
    main()
