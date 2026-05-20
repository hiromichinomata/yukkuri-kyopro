class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unite(self, a: int, b: int) -> bool:
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True


def kruskal(n: int, edges: list) -> int:
    edges.sort(key=lambda e: e[2])
    dsu = DSU(n)
    total = used = 0
    for u, v, w in edges:
        if dsu.unite(u, v):
            total += w
            used += 1
            if used == n - 1:
                break
    return total


def main() -> None:
    edges = [(0, 1, 1), (1, 2, 2), (0, 2, 4), (2, 3, 1)]
    print(kruskal(4, edges))


if __name__ == "__main__":
    main()
