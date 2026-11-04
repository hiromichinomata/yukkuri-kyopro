import sys


def main() -> None:
    t, n = map(int, sys.stdin.readline().split())
    # 税抜き A が 100 増えると、税込みはちょうど 100 + t 増える（周期性）。
    # 1 周期（A = 1〜100）の税込み価格を並べると、1〜(100+t) のうち t 個が抜ける
    prices = {(100 + t) * a // 100 for a in range(1, 101)}
    missing = [v for v in range(1, 100 + t + 1) if v not in prices]
    q, r = divmod(n - 1, t)  # 何周目の何番目か
    print(q * (100 + t) + missing[r])


if __name__ == "__main__":
    main()
