def mo_order(queries, block):
    ordered = []
    for idx, (l, r) in enumerate(queries):
        bid = l // block
        ordered.append((bid, r if bid % 2 else -r, l, r, idx))
    ordered.sort()
    return ordered


def mo_count_distinct(a, queries):
    n = len(a)
    block = int(n**0.5) + 1
    order = mo_order(queries, block)
    cnt = {}
    cur_l, cur_r = 0, 0
    distinct = 0
    ans = [0] * len(queries)

    def add(i):
        nonlocal distinct
        x = a[i]
        cnt[x] = cnt.get(x, 0) + 1
        if cnt[x] == 1:
            distinct += 1

    def remove(i):
        nonlocal distinct
        x = a[i]
        cnt[x] -= 1
        if cnt[x] == 0:
            distinct -= 1

    for _, _, l, r, idx in order:
        while cur_r <= r:
            add(cur_r)
            cur_r += 1
        while cur_r - 1 > r:
            cur_r -= 1
            remove(cur_r)
        while cur_l > l:
            cur_l -= 1
            add(cur_l)
        while cur_l < l:
            remove(cur_l)
            cur_l += 1
        ans[idx] = distinct
    return ans


def main() -> None:
    a = [1, 2, 1, 3, 2, 1, 2]
    queries = [(0, 6), (2, 5), (1, 4)]
    print(mo_count_distinct(a, queries))


if __name__ == "__main__":
    main()
