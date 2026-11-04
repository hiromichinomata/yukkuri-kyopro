import sys


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unite(self, a: int, b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dsu = DSU(n)
    for _ in range(m):
        a, b = map(int, input().split())
        dsu.unite(a - 1, b - 1)
    # 友達グループの人は全員別のグループに分ける必要がある
    # → 一番大きい友達グループの人数が答え
    print(max(dsu.size[dsu.find(v)] for v in range(n)))


if __name__ == "__main__":
    main()
