import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    iv = sorted(tuple(map(int, input().split())) for _ in range(n))  # 左端の順に並べる
    out = []
    cur_l, cur_r = iv[0]
    for l, r in iv[1:]:
        if l <= cur_r:  # 重なる・接する（半開区間 [l, r) なので l == cur_r もつながる）
            cur_r = max(cur_r, r)
        else:
            out.append(f"{cur_l} {cur_r}")
            cur_l, cur_r = l, r
    out.append(f"{cur_l} {cur_r}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
