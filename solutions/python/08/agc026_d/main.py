import sys

MOD = 10**9 + 7


def solve(h, l, r, base):
    """列 l..r の、高さ base より上の部分の塗り方を返す: (最下行が交互の塗り方の数, 全体の数)"""
    mh = min(h[l : r + 1])
    height = mh - base  # 全列にまたがる長方形部分の行数
    # mh より高い部分は、連続した区間ごとに再帰
    subs = []
    free_cols = 0
    i = l
    while i <= r:
        if h[i] == mh:
            free_cols += 1
            i += 1
            continue
        j = i
        while j + 1 <= r and h[j + 1] > mh:
            j += 1
        subs.append(solve(h, i, j, mh))
        i = j + 1
    prod_alt = 1  # Π a_k
    prod_sum = 1  # Π (a_k + b_k)
    for a, b in subs:
        prod_alt = prod_alt * a % MOD
        prod_sum = prod_sum * (a + b) % MOD
    # 1 行が「赤青交互」なら、上下の行も交互（位相は自由）。交互でない行は、上下の行がその反転に決まる。
    # ただし「交互か」は、その上の区間 S_k の列だけで見ればよい（制約は S_k の中の隣り合う列にしかない）。
    #   長方形の最上行 P が交互: 長方形の各行 2 通り、S_k は最下行が交互なら何でもよい → 2^height × Π a_k
    #   P が交互でない: 長方形は P で決まる。S_k の最下行は、P|S_k が交互なら交互の塗り方（a_k 通り）、
    #     交互でなければ P|S_k の反転に決まる。P を全パターンで足すと列ごとに独立になり
    #     S_k ごとに「交互の 2 パターン × a_k/2 ＋ 交互でない分 b_k − a_k」= a_k + b_k。
    #     そこから P 全体が交互の 2 パターン（各 Π a_k）を引く
    alt = pow(2, height, MOD) * prod_alt % MOD
    non_alt = (pow(2, free_cols, MOD) * prod_sum - 2 * prod_alt) % MOD
    return alt, (alt + non_alt) % MOD


def main() -> None:
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    n = int(data[0])
    h = [int(x) for x in data[1 : 1 + n]]
    print(solve(h, 0, n - 1, 0)[1])


if __name__ == "__main__":
    main()
