import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    a = [int(x) for x in data[2 : 2 + n]]
    # 言い換え: 値 v のボールが c 個あると、魔法で「ボールが v 個 → v-c 個」に一気に進める。
    # つまり区間 (v-c, v] を覆う。位置 1〜N がすべて覆われていれば全部消せる。
    # 覆われていない位置 1 つにつき 1 個書き換えればよいので、答えは「覆われていない位置の数」
    cnt = [0] * (n + 1)  # cnt[v]: 値 v のボールの数
    cover = [0] * (n + 1)  # cover[p]: 位置 p を覆う回数
    for v in a:
        cnt[v] += 1
        p = v - cnt[v] + 1  # 値 v の k 個目のボールは位置 v-k+1 を覆う
        if p >= 1:
            cover[p] += 1
    zeros = sum(1 for p in range(1, n + 1) if cover[p] == 0)

    def change(p, d):
        nonlocal zeros
        if p < 1:
            return
        if cover[p] == 0:
            zeros -= 1
        cover[p] += d
        if cover[p] == 0:
            zeros += 1

    out = []
    pos = 2 + n
    for j in range(m):
        x, y = int(data[pos + 2 * j]) - 1, int(data[pos + 2 * j + 1])
        old = a[x]
        change(old - cnt[old] + 1, -1)  # 値 old の最後のボールが覆っていた位置
        cnt[old] -= 1
        cnt[y] += 1
        change(y - cnt[y] + 1, 1)
        a[x] = y
        out.append(zeros)
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    main()
