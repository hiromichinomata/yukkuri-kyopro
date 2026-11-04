import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    x, y, z = int(data[0]), int(data[1]), int(data[2])
    n = x + y + z
    people = []
    base = 0
    for i in range(n):
        a, b, c = (int(v) for v in data[3 + 3 * i : 6 + 3 * i])
        base += a  # いったん全員から金貨をもらったことにして、銀・銅に替えたときの増減だけ考える
        people.append((b - a, c - a))
    # 「銀にする得 − 銅にする得」が大きい順に並べると、銀をもらう人はすべて銅をもらう人より前に来る
    # （入れ替えると得が減らない）。だから境界 k を決めて、前 k 人から Y 人を銀、後ろから Z 人を銅に選ぶ
    people.sort(key=lambda p: p[0] - p[1], reverse=True)
    # pre[k]: 前 k 人から銀の得が大きい Y 人を選んだ和（ヒープで大きい Y 個を保つ）
    pre = [None] * (n + 1)
    h, s = [], 0
    for k in range(n):
        heapq.heappush(h, people[k][0])
        s += people[k][0]
        if len(h) > y:
            s -= heapq.heappop(h)
        if len(h) == y:
            pre[k + 1] = s
    # suf[k]: k 人目以降から銅の得が大きい Z 人を選んだ和
    suf = [None] * (n + 1)
    h, s = [], 0
    for k in range(n - 1, -1, -1):
        heapq.heappush(h, people[k][1])
        s += people[k][1]
        if len(h) > z:
            s -= heapq.heappop(h)
        if len(h) == z:
            suf[k] = s
    best = max(pre[k] + suf[k] for k in range(y, n - z + 1))
    print(base + best)


if __name__ == "__main__":
    main()
