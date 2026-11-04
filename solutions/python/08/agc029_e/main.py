import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    g = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        g[a].append(b)
        g[b].append(a)
    # 1 を根にする。m[v]: v の親から根までの道の最大 ID（m[1] = 0）
    parent = [0] * (n + 1)
    m = [0] * (n + 1)
    order = [1]
    parent[1] = -1
    for v in order:
        for c in g[v]:
            if c != parent[v]:
                parent[c] = v
                m[c] = max(m[v], v)
                order.append(c)
    children = [[c for c in g[v] if c != parent[v]] for v in range(n + 1)]

    memo = {}

    def q(v, x):
        """v の子孫のうち、x 未満の ID だけを通って v から行ける頂点の数。
        途中でたどった頂点 u についても (u, x) の値をメモする（帰りがけ順で足し上げる）"""
        if (v, x) in memo:
            return memo[(v, x)]
        stack = [(v, False)]
        while stack:
            u, done = stack.pop()
            if done:
                memo[(u, x)] = sum(1 + memo[(c, x)] for c in children[u] if c < x)
                continue
            stack.append((u, True))
            for c in children[u]:
                if c < x and (c, x) not in memo:
                    stack.append((c, False))
        return memo[(v, x)]

    # c[v] - c[parent]: v が親の道の最大より大きいかで場合分け（公式解説）
    c = [0] * (n + 1)
    c[1] = 1
    for v in order[1:]:
        p = parent[v]
        if v > m[p]:
            c[v] = c[p] + q(v, m[v]) + 1
        else:
            c[v] = c[p] + q(v, m[v]) - q(v, m[p])
    print(*(c[v] - 1 for v in range(2, n + 1)))


if __name__ == "__main__":
    main()
