import sys
from collections import deque


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    edges = [tuple(int(x) - 1 for x in input().split()) for _ in range(n - 1)]
    g = [[] for _ in range(n)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    # 頂点 0 を根にして親と訪問順を求める
    parent = [-1] * n
    order = []
    seen = [False] * n
    seen[0] = True
    q = deque([0])
    while q:
        v = q.popleft()
        order.append(v)
        for to in g[v]:
            if not seen[to]:
                seen[to] = True
                parent[to] = v
                q.append(to)
    add = [0] * n  # add[v]: v の部分木全体に足す値（最後に根から累積する）
    for _ in range(int(input())):
        t, e, x = map(int, input().split())
        a, b = edges[e - 1]
        if t == 2:
            a, b = b, a  # 「b を通らずに a から行ける頂点」に足す、に統一
        if parent[a] == b:
            add[a] += x  # a が子 → a の部分木だけ
        else:
            add[0] += x  # a が親 → b の部分木以外全部 = 全体に足して b の部分木から引く
            add[b] -= x
    for v in order[1:]:  # 根から順に、親の値を子へ足し込む（木の上の累積和）
        add[v] += add[parent[v]]
    print("\n".join(map(str, add)))


if __name__ == "__main__":
    main()
