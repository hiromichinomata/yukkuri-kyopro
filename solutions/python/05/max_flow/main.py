from collections import deque


def max_flow(cap: list, s: int, t: int, n: int) -> int:
    flow = 0
    while True:
        parent = [-1] * n
        parent[s] = s
        q = deque([s])
        while q:
            v = q.popleft()
            for to in range(n):
                if parent[to] == -1 and cap[v][to] > 0:
                    parent[to] = v
                    q.append(to)
        if parent[t] == -1:
            break
        f = 10**18
        v = t
        while v != s:
            f = min(f, cap[parent[v]][v])
            v = parent[v]
        v = t
        while v != s:
            u = parent[v]
            cap[u][v] -= f
            cap[v][u] += f
            v = u
        flow += f
    return flow


def main() -> None:
    n = 4
    cap = [[0] * n for _ in range(n)]
    cap[0][1] = 3
    cap[0][2] = 2
    cap[1][2] = 1
    cap[1][3] = 2
    cap[2][3] = 3
    print(max_flow(cap, 0, 3, n))


if __name__ == "__main__":
    main()
