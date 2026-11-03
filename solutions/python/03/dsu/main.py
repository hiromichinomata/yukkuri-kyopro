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

    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


def main() -> None:
    dsu = DSU(5)
    dsu.unite(0, 1)
    dsu.unite(2, 3)
    print(dsu.same(0, 1), dsu.same(0, 2))


if __name__ == "__main__":
    main()
