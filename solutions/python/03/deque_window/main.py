from collections import deque


def max_sum_k(xs: list, k: int) -> int:
    q = deque()
    s = 0
    ans = -10**18
    for i, x in enumerate(xs):
        s += x
        q.append(i)
        if len(q) > k:
            s -= xs[q.popleft()]
        if i >= k - 1:
            ans = max(ans, s)
    return ans


def main() -> None:
    xs = [1, 2, 3, 4, 5]
    print(max_sum_k(xs, 3))


if __name__ == "__main__":
    main()
