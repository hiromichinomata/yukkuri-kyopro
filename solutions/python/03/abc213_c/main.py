import bisect
import sys


def main() -> None:
    input = sys.stdin.readline
    h, w, n = map(int, input().split())
    cards = [tuple(map(int, input().split())) for _ in range(n)]
    # 数字のある行・列だけが残る → 行番号・列番号をそれぞれ座標圧縮すればよい
    rows = sorted({a for a, _ in cards})
    cols = sorted({b for _, b in cards})
    out = [f"{bisect.bisect_left(rows, a) + 1} {bisect.bisect_left(cols, b) + 1}" for a, b in cards]
    print("\n".join(out))


if __name__ == "__main__":
    main()
