import sys

MAX = 10**5


def main() -> None:
    input = sys.stdin.readline
    # エラトステネスの篩
    is_prime = [True] * (MAX + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX + 1, i):
                is_prime[j] = False
    # cnt[x]: x 以下の「2017 に似た数」の個数（累積和）
    cnt = [0] * (MAX + 1)
    for x in range(1, MAX + 1):
        like = x % 2 == 1 and is_prime[x] and is_prime[(x + 1) // 2]
        cnt[x] = cnt[x - 1] + like
    q = int(input())
    out = []
    for _ in range(q):
        l, r = map(int, input().split())
        out.append(cnt[r] - cnt[l - 1])
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    main()
