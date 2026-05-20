from collections import deque


class Dinic:
    def __init__(self, n: int) -> None:
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr: int, to: int, cap: int) -> None:
        self.g[fr].append([to, cap, len(self.g[to])])
        self.g[to].append([fr, 0, len(self.g[fr]) - 1])

    def bfs(self, s: int, t: int, level: list) -> bool:
        for i in range(self.n):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for to, cap, _ in self.g[v]:
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        return level[t] >= 0

    def dfs(self, v: int, t: int, f: int, level: list, iter_: list) -> int:
        if v == t:
            return f
        for i in range(iter_[v], len(self.g[v])):
            iter_[v] = i
            to, cap, rev = self.g[v][i]
            if cap > 0 and level[v] < level[to]:
                d = self.dfs(to, t, min(f, cap), level, iter_)
                if d > 0:
                    self.g[v][i][1] -= d
                    self.g[to][rev][1] += d
                    return d
        return 0

    def max_flow(self, s: int, t: int) -> int:
        flow = 0
        level = [-1] * self.n
        while self.bfs(s, t, level):
            iter_ = [0] * self.n
            while True:
                f = self.dfs(s, t, 10**18, level, iter_)
                if f == 0:
                    break
                flow += f
        return flow


def main() -> None:
    n = 4
    dinic = Dinic(n)
    dinic.add_edge(0, 1, 3)
    dinic.add_edge(0, 2, 2)
    dinic.add_edge(1, 2, 1)
    dinic.add_edge(1, 3, 2)
    dinic.add_edge(2, 3, 3)
    print(dinic.max_flow(0, 3))


if __name__ == "__main__":
    main()
