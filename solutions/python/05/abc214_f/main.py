import sys

MOD = 10**9 + 7


def main() -> None:
    s = sys.stdin.readline().strip()
    n = len(s)
    # 同じ文字列 T を二重に数えないため、T を「できるだけ左の位置」で選ぶ選び方だけを数える。
    # dp[i]: 最後に選んだ文字が位置 i（1 始まり）である文字列の数。dp[0] は「まだ何も選んでいない」
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        c = s[i - 1]
        total = 0
        ok = True
        # 1 つ前に選んだ位置 p を、i に近い方から見る（隣は選べないので p ≤ i - 2）。
        # p+2〜i-1 に c があると、c をもっと左で選べる → 「できるだけ左」ではないので打ち切る
        for p in range(i - 2, 0, -1):
            if p + 2 <= i - 1 and s[p + 1] == c:  # p を 1 つ減らすと、位置 p+2 が新たに範囲に入る
                ok = False
                break
            total += dp[p]
        # 何も選んでいない状態から c を選ぶ: 位置 1〜i-1 に c がなければよい
        # （3〜i-1 は上のループで確認済みなので、残りは位置 1 と 2）
        if ok and all(s[q - 1] != c for q in (1, 2) if q <= i - 1):
            total += dp[0]
        dp[i] = total % MOD
    print(sum(dp[1:]) % MOD)


if __name__ == "__main__":
    main()
