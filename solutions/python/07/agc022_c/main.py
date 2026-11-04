import sys

MAXV = 50


def reachable(allowed: set) -> list:
    """reach[v][w]: v から、allowed の k で余りを取る操作を繰り返して w にできるか"""
    reach = [[v == w for w in range(MAXV + 1)] for v in range(MAXV + 1)]
    for v in range(MAXV + 1):
        for k in allowed:
            reach[v][v % k] = True
    for mid in range(MAXV + 1):  # ワーシャルフロイドで推移閉包
        for v in range(MAXV + 1):
            if reach[v][mid]:
                rv, rm = reach[v], reach[mid]
                for w in range(MAXV + 1):
                    if rm[w]:
                        rv[w] = True
    return reach


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    def ok(allowed):
        r = reachable(allowed)
        return all(r[x][y] for x, y in zip(a, b))

    allowed = set(range(1, MAXV + 1))
    if not ok(allowed):
        print(-1)
        return
    # 2^k は 2^1 + ... + 2^(k-1) より大きいので、大きい k から「使わずに済むか」を決める
    for k in range(MAXV, 0, -1):
        allowed.discard(k)
        if not ok(allowed):
            allowed.add(k)
    print(sum(1 << k for k in allowed))


if __name__ == "__main__":
    main()
