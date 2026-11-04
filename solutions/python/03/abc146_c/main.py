import sys


def main() -> None:
    a, b, x = map(int, sys.stdin.readline().split())

    def can_buy(n: int) -> bool:
        return a * n + b * len(str(n)) <= x

    ok, ng = 0, 10**9 + 1  # ok: 買える（0 は「何も買えない」の番兵）, ng: 買えない
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if can_buy(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
