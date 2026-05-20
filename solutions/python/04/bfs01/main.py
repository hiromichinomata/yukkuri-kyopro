from collections import deque


def bfs01(g, start, n):
    INF = 10**18
    dist = [INF] * n
    dist[start] = 0
    dq = deque([start])
    while dq:
        v = dq.popleft()
        for to, cost in g[v]:
            nd = dist[v] + cost
            if nd < dist[to]:
                dist[to] = nd
                if cost == 0:
                    dq.appendleft(to)
                else:
                    dq.append(to)
    return dist


def main() -> None:
    n = 4
    g = [[] for _ in range(n)]
    g[0].append((1, 0))
    g[1].append((0, 0))
    g[1].append((2, 1))
    g[2].append((1, 1))
    g[2].append((3, 0))
    g[3].append((2, 0))
    print(bfs01(g, 0, n))


if __name__ == "__main__":
    main()
