def subset_sum_pruned(xs, target):
    xs = sorted(xs, reverse=True)
    best = [False]

    def dfs(i, rem):
        if rem == 0:
            best[0] = True
            return
        if rem < 0 or i == len(xs):
            return
        if sum(xs[i:]) < rem:
            return
        dfs(i + 1, rem - xs[i])
        if best[0]:
            return
        dfs(i + 1, rem)

    dfs(0, target)
    return best[0]


def main() -> None:
    xs = [3, 7, 8, 2, 5]
    for t in [10, 11, 23, 24]:
        print(t, subset_sum_pruned(xs, t))


if __name__ == "__main__":
    main()
