def build_next(p: str) -> list:
    m = len(p)
    nxt = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = nxt[j - 1]
        if p[i] == p[j]:
            j += 1
            nxt[i] = j
    return nxt


def kmp_search(text: str, pat: str) -> list:
    nxt = build_next(pat)
    j = 0
    pos = []
    for i in range(len(text)):
        while j > 0 and text[i] != pat[j]:
            j = nxt[j - 1]
        if text[i] == pat[j]:
            j += 1
        if j == len(pat):
            pos.append(i - len(pat) + 1)
            j = nxt[j - 1]
    return pos


def main() -> None:
    print(kmp_search("ababaabab", "aba"))


if __name__ == "__main__":
    main()
