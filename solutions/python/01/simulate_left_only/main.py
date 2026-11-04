import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    xs = list(map(int, input().split()))
    score = [0, 0]  # score[0]: 先手, score[1]: 後手
    turn = 0
    i = 0
    while i < n:  # 左端から 1 枚ずつ取る
        score[turn] += xs[i]
        i += 1
        turn ^= 1  # 手番の交代は 1 か所で
    print(score[0] - score[1])


if __name__ == "__main__":
    main()
