import sys
from collections import deque


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    # 条件 i は「A_P ≥ X ⇔ A_Q ≥ Y」かつ「A_P ≥ X+1 ⇔ A_Q ≥ Y+1」と同じ。
    # これを 4 本の含意「A_u ≥ t ならば A_w ≥ s」にして、各頂点 u ごとに t の小さい順に並べる
    rules = [[] for _ in range(n)]
    for i in range(k):
        p, x, q, y = (int(v) for v in data[3 + 4 * i : 7 + 4 * i])  # 入力は P X Q Y の順
        p -= 1
        q -= 1
        rules[p].append((x, q, y))
        rules[q].append((y, p, x))
        rules[p].append((x + 1, q, y + 1))
        rules[q].append((y + 1, p, x + 1))
    for r in rules:
        r.sort()
    a = [1] * n  # すべて 1 から始め、必要な分だけ値を上げていく（上げ方は最小限）
    ptr = [0] * n  # rules[u] のうち、すでに発動した含意の数
    q = deque(range(n))
    while q:
        u = q.popleft()
        r = rules[u]
        while ptr[u] < len(r) and r[ptr[u]][0] <= a[u]:
            _, w, s = r[ptr[u]]
            ptr[u] += 1
            if a[w] < s:
                a[w] = s
                if s > m:  # M を超えたら満たす数列はない
                    print(-1)
                    return
                q.append(w)
    print(sum(a))


if __name__ == "__main__":
    main()
