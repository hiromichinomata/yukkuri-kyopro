import sys


def main() -> None:
    input = sys.stdin.readline
    n, q = map(int, input().split())
    diff = [0] * (n + 1)  # いもす法: 区間 [l, r] に +1 → diff[l-1] += 1, diff[r] -= 1
    for _ in range(q):
        l, r = map(int, input().split())
        diff[l - 1] += 1
        diff[r] -= 1
    out = []
    cnt = 0
    for i in range(n):
        cnt += diff[i]  # 駒 i が裏返された回数
        out.append("1" if cnt % 2 else "0")  # 奇数回なら白（1）
    print("".join(out))


if __name__ == "__main__":
    main()
