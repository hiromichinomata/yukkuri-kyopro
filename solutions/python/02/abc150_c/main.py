import itertools
import sys


def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    # permutations は辞書順に列挙するので、何番目に出てくるかを数えればよい
    a = b = 0
    for k, perm in enumerate(itertools.permutations(range(1, n + 1))):
        if perm == p:
            a = k
        if perm == q:
            b = k
    print(abs(a - b))


if __name__ == "__main__":
    main()
