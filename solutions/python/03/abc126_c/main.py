import sys


def main() -> None:
    n, k = map(int, sys.stdin.readline().split())
    total = 0.0
    for start in range(1, n + 1):  # サイコロの目ごとに勝つ確率を足す
        score, p = start, 1.0
        while score < k:  # K 以上になるまで表を出し続ける必要がある
            score *= 2
            p /= 2
        total += p
    print(f"{total / n:.12f}")


if __name__ == "__main__":
    main()
