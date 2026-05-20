from collections import deque


def topological_sort(n: int, g: list, indeg: list) -> list:
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for to in g[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)
    return order


def main() -> None:
    n = 4
    g = [[1, 2], [3], [3], []]
    indeg = [0, 1, 1, 2]
    print(topological_sort(n, g, indeg))


if __name__ == "__main__":
    main()
