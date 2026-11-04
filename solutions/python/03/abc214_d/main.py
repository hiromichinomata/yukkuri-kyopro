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
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    edges = sorted((w, u - 1, v - 1) for u, v, w in (map(int, input().split()) for _ in range(n - 1)))
    dsu = DSU(n)
    ans = 0
    # 重みの小さい辺から順につなぐ。辺 (u, v, w) をつないだ瞬間に初めて行き来できるようになる
    # 頂点の組は size[u 側] × size[v 側] 組あり、その組の f はちょうど w（主客転倒）
    for w, u, v in edges:
        ans += w * dsu.size[dsu.find(u)] * dsu.size[dsu.find(v)]
        dsu.unite(u, v)
    print(ans)


if __name__ == "__main__":
    main()
