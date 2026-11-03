import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = [int(input()) for _ in range(n)]
    # 自分以外の最大値は、自分が 1 番大きい値でなければ 1 番大きい値、そうなら 2 番目
    first = max(a)
    i_first = a.index(first)
    second = max(a[:i_first] + a[i_first + 1 :])
    out = [second if i == i_first else first for i in range(n)]
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    main()
