import sys


def main() -> None:
    n = int(sys.stdin.readline())
    # 連結成分に k 頂点入っているとき、外の頂点を選ぶ確率は (n-k)/n。
    # 成功確率 p の試行を成功まで繰り返す回数の期待値は 1/p なので、
    # k = 1, ..., n-1 の n/(n-k) を足す（期待値の線形性）
    ans = sum(n / (n - k) for k in range(1, n))
    print(f"{ans:.10f}")


if __name__ == "__main__":
    main()
