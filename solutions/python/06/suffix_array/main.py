def suffix_array(s: str) -> list:
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    k = 1
    while k < n:
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
        new_rank = [0] * n
        new_rank[sa[0]] = 0
        for i in range(1, n):
            a = (rank[sa[i]], rank[sa[i] + k] if sa[i] + k < n else -1)
            b = (rank[sa[i - 1]], rank[sa[i - 1] + k] if sa[i - 1] + k < n else -1)
            new_rank[sa[i]] = new_rank[sa[i - 1]] + (a < b)
        rank = new_rank
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1
    return sa


def main() -> None:
    s = "banana"
    sa = suffix_array(s)
    print(sa)
    print([s[i:] for i in sa])


if __name__ == "__main__":
    main()
