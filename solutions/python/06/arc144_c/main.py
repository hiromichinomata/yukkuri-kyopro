import sys


def base(length: int, k: int) -> list:
    """2K ≤ length ≤ 4K のときの辞書順最小（1 始まりの値で返す）"""
    a = [0] * (length + 1)
    if length <= 3 * k:
        for i in range(1, length + 1):
            a[i] = i + k if i <= length - k else i - length + k
    else:
        for i in range(1, length + 1):
            if i <= k:
                a[i] = i + k
            elif i <= length - 2 * k:
                a[i] = i - k
            elif i <= length - k:
                a[i] = i + k
            elif i <= 3 * k:
                a[i] = i - 2 * k
            else:
                a[i] = i - k
    return a[1:]


def main() -> None:
    n, k = map(int, sys.stdin.readline().split())
    if n < 2 * k:  # A_1 は K+1 以上、A_N は N-K 以下… と詰めると N ≥ 2K が必要
        print(-1)
        return
    ans = []
    offset = 0
    # 残りが 4K を超える間は、先頭 2K 個を (K+1, …, 2K, 1, …, K) で埋めるのが辞書順最小
    while n - offset > 4 * k:
        ans += [offset + v for v in list(range(k + 1, 2 * k + 1)) + list(range(1, k + 1))]
        offset += 2 * k
    ans += [offset + v for v in base(n - offset, k)]  # 残り（2K〜4K 個）は場合分けで埋める
    print(*ans)


if __name__ == "__main__":
    main()
