import sys


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    solved = [False] * (n + 1)
    wa = [0] * (n + 1)  # 最初の AC までの WA の数
    for _ in range(m):
        p, s = input().split()
        p = int(p)
        if solved[p]:
            continue  # AC 後の提出は数えない
        if s == "AC":
            solved[p] = True
        else:
            wa[p] += 1
    ac = sum(solved)
    penalty = sum(wa[p] for p in range(1, n + 1) if solved[p])  # AC した問題の WA だけ
    print(ac, penalty)


if __name__ == "__main__":
    main()
