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

    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


def main() -> None:
    input = sys.stdin.readline
    n, q = map(int, input().split())
    dsu = DSU(n)
    out = []
    for _ in range(q):
        t, u, v = map(int, input().split())
        u -= 1
        v -= 1
        if t == 1:
            dsu.unite(u, v)
        else:
            out.append("Yes" if dsu.same(u, v) else "No")
    print("\n".join(out))


if __name__ == "__main__":
    main()
