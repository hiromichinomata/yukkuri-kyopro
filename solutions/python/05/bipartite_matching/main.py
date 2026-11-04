import sys


def max_matching(n_left: int, n_right: int, g: list) -> int:
    """二部グラフの最大マッチング（増加路 DFS、O(V E)）。g[u] は左 u から行ける右の頂点"""
    match_r = [-1] * n_right  # 右 v の相手（左の番号）、いなければ -1

    def try_kuhn(u: int, seen: list) -> bool:
        for v in g[u]:
            if seen[v]:
                continue
            seen[v] = True
            # v が空いている、または v の今の相手を別の右頂点に移せるなら u と組める
            if match_r[v] == -1 or try_kuhn(match_r[v], seen):
                match_r[v] = u
                return True
        return False

    result = 0
    for u in range(n_left):
        if try_kuhn(u, [False] * n_right):
            result += 1
    return result


def main() -> None:
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    n_left, n_right, m = map(int, input().split())
    g = [[] for _ in range(n_left)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
    print(max_matching(n_left, n_right, g))


if __name__ == "__main__":
    main()
