import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    s = input().strip()
    x = int(input())
    ans = []
    for ch in s:
        if "A" <= ch <= "Z":
            c = (ord(ch) - ord("A") + x) % 26
            ans.append(chr(ord("A") + c))
        else:
            ans.append(ch)
    print("".join(ans))


if __name__ == "__main__":
    main()
