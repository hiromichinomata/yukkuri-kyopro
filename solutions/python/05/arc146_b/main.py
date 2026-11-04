import sys


def cost(a: int, target: int) -> int:
    """a 以上で、target の 1 のビットをすべて持つ最小の数にするのに必要な +1 の回数"""
    if a & target == target:
        return 0
    # target にあって a にない、いちばん上のビット h を見つける
    h = (target & ~a).bit_length() - 1
    # h より上は a のまま、h を立て、h より下は target の分だけにする
    upper = (a >> (h + 1)) << (h + 1)
    x = upper | (1 << h) | (target & ((1 << h) - 1))
    return x - a


def main() -> None:
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for b in range(30, -1, -1):  # 上のビットから「立てられるか」を貪欲に決める
        cand = ans | (1 << b)
        costs = sorted(cost(x, cand) for x in a)
        if sum(costs[:k]) <= m:  # 安い K 個に操作を集中させる
            ans = cand
    print(ans)


if __name__ == "__main__":
    main()
