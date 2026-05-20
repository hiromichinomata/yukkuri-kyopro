import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    xs = list(map(int, input().split()))
    t = 0
    while xs:
        t += xs.pop(0)
    print(t)


if __name__ == "__main__":
    main()
