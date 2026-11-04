import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    h = list(map(int, input().split()))
    prev = 0  # 直前のマスの（操作後の）高さ
    for x in h:
        if x - 1 >= prev:  # 下げても大丈夫なら下げる（後ろが楽になる）
            prev = x - 1
        elif x >= prev:  # 下げられないならそのまま
            prev = x
        else:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
