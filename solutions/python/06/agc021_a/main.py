import sys


def main() -> None:
    s = sys.stdin.readline().strip()
    best = sum(map(int, s))  # N そのもの
    for i, ch in enumerate(s):
        if ch == "0":
            continue
        # i 桁目を 1 減らし、それより下を全部 9 にした数は N 以下
        cand = sum(map(int, s[:i])) + int(ch) - 1 + 9 * (len(s) - i - 1)
        best = max(best, cand)
    print(best)


if __name__ == "__main__":
    main()
