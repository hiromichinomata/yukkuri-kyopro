from collections import deque


def is_bipartite(g, n):
    color = [-1] * n
    for s in range(n):
        if color[s] != -1:
            continue
        color[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for to in g[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                elif color[to] == color[v]:
                    return False
    return True


def main() -> None:
    g = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(is_bipartite(g, 4))
    g2 = [[1, 2], [0, 2], [0, 1]]
    print(is_bipartite(g2, 3))


if __name__ == "__main__":
    main()
