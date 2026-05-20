import heapq


def dijkstra(g: list, start: int, n: int) -> list:
    INF = 10**18
    dist = [INF] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for to, cost in g[v]:
            nd = d + cost
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(pq, (nd, to))
    return dist


def main() -> None:
    n = 4
    g = [[] for _ in range(n)]
    edges = [(0, 1, 1), (0, 2, 4), (1, 2, 2), (1, 3, 6), (2, 3, 1)]
    for u, v, c in edges:
        g[u].append((v, c))
        g[v].append((u, c))
    print(dijkstra(g, 0, n)[3])


if __name__ == "__main__":
    main()
