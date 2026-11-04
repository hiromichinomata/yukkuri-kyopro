import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    s = input().strip()
    ans = []
    for ch in s:
        c = (ord(ch) - ord("A") + n) % 26  # Z の次は A
        ans.append(chr(ord("A") + c))
    print("".join(ans))


if __name__ == "__main__":
    main()
