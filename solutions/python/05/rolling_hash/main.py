import random
import sys

MOD = (1 << 61) - 1
BASE = random.randrange(10**5, MOD - 1)  # 基数はランダムに選ぶ（狙い撃ちの衝突を防ぐ）


class RollingHash:
    def __init__(self, s: str) -> None:
        n = len(s)
        self.h = [0] * (n + 1)  # h[i] = s[0:i] のハッシュ
        self.pw = [1] * (n + 1)  # pw[i] = BASE^i
        for i, ch in enumerate(s):
            self.h[i + 1] = (self.h[i] * BASE + ord(ch)) % MOD
            self.pw[i + 1] = self.pw[i] * BASE % MOD

    def get(self, l: int, r: int) -> int:
        """s[l:r] のハッシュを O(1) で返す"""
        return (self.h[r] - self.h[l] * self.pw[r - l]) % MOD


def count_occurrences(t: str, p: str) -> int:
    if len(p) > len(t):
        return 0
    ht, hp = RollingHash(t), RollingHash(p)
    target = hp.get(0, len(p))
    return sum(1 for i in range(len(t) - len(p) + 1) if ht.get(i, i + len(p)) == target)


def main() -> None:
    input = sys.stdin.readline
    t = input().strip()
    p = input().strip()
    print(count_occurrences(t, p))
    rh = RollingHash(t)
    # t[0:3] と t[7:10] が等しいかを O(1) で比べる
    print("Yes" if rh.get(0, 3) == rh.get(7, 10) else "No")


if __name__ == "__main__":
    main()
