import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n, m = int(next(it)), int(next(it))
        a = b = 0  # 直前までの A と B（A_0 = B_0 = 0）
        best = None
        for _ in range(n):
            x, y = int(next(it)), int(next(it))
            # この区間で k 個進んだとき: B_k = b + x k、A_k = a + b k + x k(k+1)/2（k = 1〜y）
            cand = [1, y]
            # A は B_k > 0 の間だけ増える。x < 0 なら B_k が正である最後の k で A が最大
            if x < 0 and b > 0:
                k = b // (-x)
                if 1 <= k <= y:
                    cand.append(k)
            for k in cand:
                v = a + b * k + x * k * (k + 1) // 2
                if best is None or v > best:
                    best = v
            a += b * y + x * y * (y + 1) // 2
            b += x * y
        out.append(best)
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    main()
