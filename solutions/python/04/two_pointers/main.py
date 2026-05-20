def count_subarray_le_k(xs, k):
    n = len(xs)
    ans = left = s = 0
    for right in range(n):
        s += xs[right]
        while s > k and left <= right:
            s -= xs[left]
            left += 1
        ans += right - left + 1
    return ans


def main() -> None:
    print(count_subarray_le_k([1, 2, 3, 4], 5))


if __name__ == "__main__":
    main()
