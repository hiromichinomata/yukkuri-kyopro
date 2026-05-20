def kth(arr, l, r, k):
    """[l, r) の k 番目（0-indexed）。本番は Wavelet Tree で O(log sigma)"""
    return sorted(arr[l:r])[k]


def main() -> None:
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(kth(arr, 0, 8, 3))
    print(kth(arr, 2, 6, 1))


if __name__ == "__main__":
    main()
