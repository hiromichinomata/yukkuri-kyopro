import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[j] - a[i] == a[k] - a[j]:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
