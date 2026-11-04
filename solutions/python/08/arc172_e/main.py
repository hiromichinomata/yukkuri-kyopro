import sys

MOD9 = 10**9


def solve(x: int) -> int:
    # k ≥ 2 では、n^n mod 10^k は n mod 10^k だけで決まる
    # （λ(10^k) が 10^k を割り切るので、n を 10^k 増やしても指数の分は変わらない）。
    # そこで mod 100 の候補から始めて、1 桁ずつ上に伸ばす
    cands = [n for n in range(1, 101) if pow(n, n, 100) == x % 100]
    m = 100
    for _ in range(7):  # 10^2 → 10^9
        nm = m * 10
        nxt = []
        for c in cands:
            for d in range(10):
                n = c + d * m
                if n > 0 and pow(n, n, nm) == x % nm:
                    nxt.append(n)
        cands = nxt
        m = nm
    # n mod 10^9 が同じなら n^n mod 10^9 も同じ → 最小の n は 10^9 未満の候補の最小
    return min(cands) if cands else -1


def main() -> None:
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    print("\n".join(str(solve(int(x))) for x in data[1 : 1 + q]))


if __name__ == "__main__":
    main()
