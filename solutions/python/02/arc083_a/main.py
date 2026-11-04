import sys


def main() -> None:
    a, b, c, d, e, f = map(int, sys.stdin.readline().split())
    # 作れる水の量・砂糖の量を、それぞれ全部列挙する
    waters = set()
    for i in range(f // (100 * a) + 1):
        for j in range(f // (100 * b) + 1):
            w = 100 * a * i + 100 * b * j
            if 0 < w <= f:
                waters.add(w)
    sugars = set()
    for i in range(f // c + 1):
        for j in range(f // d + 1):
            s = c * i + d * j
            if s <= f:
                sugars.add(s)

    best_total, best_sugar = 100 * a, 0  # 砂糖なしの水（濃度 0）
    for w in waters:
        for s in sugars:
            if w + s > f or s * 100 > e * w:  # 容量オーバー or 溶け残り
                continue
            # s / (w+s) > best_sugar / best_total を、割り算せずに比較
            if s * best_total > best_sugar * (w + s):
                best_total, best_sugar = w + s, s
    print(best_total, best_sugar)


if __name__ == "__main__":
    main()
