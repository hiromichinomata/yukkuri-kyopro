import heapq
import sys


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    jobs = [[] for _ in range(m + 1)]  # jobs[a]: 報酬まで a 日かかる仕事の報酬
    for _ in range(n):
        a, b = map(int, input().split())
        if a <= m:
            jobs[a].append(b)

    # 締切に近い日（残り 1 日）から逆向きに見る。
    # 残り r 日の日には「a ≤ r の仕事」が候補になり、その中で最大を取る。
    heap = []
    total = 0
    for r in range(1, m + 1):
        for b in jobs[r]:
            heapq.heappush(heap, -b)  # heapq は最小ヒープなので符号反転
        if heap:
            total += -heapq.heappop(heap)
    print(total)


if __name__ == "__main__":
    main()
