import sys


def valid(s: str) -> bool:
    st = []
    pair = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            st.append(ch)
        elif ch in ")]}":
            if not st or st[-1] != pair[ch]:
                return False
            st.pop()
    return len(st) == 0


def main() -> None:
    s = sys.stdin.readline().strip()
    print("Yes" if valid(s) else "No")


if __name__ == "__main__":
    main()
