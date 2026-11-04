import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)  # 大きい順に並べる
    diff = 0  # Alice の得点 - Bob の得点
    turn = 0  # 0: Alice, 1: Bob
    for x in a:
        if turn == 0:
            diff += x
        else:
            diff -= x
        turn ^= 1
    print(diff)


if __name__ == "__main__":
    main()
