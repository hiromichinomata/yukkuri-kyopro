import sys


def main() -> None:
    s = sys.stdin.readline().strip()
    if len(s) < 26:
        # まだ使っていない文字があれば、一番小さいものを末尾に足すのが次の単語
        used = set(s)
        c = min(ch for ch in "abcdefghijklmnopqrstuvwxyz" if ch not in used)
        print(s + c)
        return
    # 26 文字全部使っているとき: 後ろから見て、s[i] をそれより後ろにある大きい文字に替えられる
    # 一番後ろの位置 i を探し、s[:i] + （s[i] より大きい文字のうち最小）
    for i in range(25, -1, -1):
        bigger = [ch for ch in s[i + 1 :] if ch > s[i]]
        if bigger:
            print(s[:i] + min(bigger))
            return
    print(-1)  # "zyx…a" は最後の単語


if __name__ == "__main__":
    main()
