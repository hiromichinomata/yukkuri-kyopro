class Fenwick:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, x: int) -> None:
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l: int, r: int) -> int:
        return self.sum(r) - self.sum(l - 1)


def main() -> None:
    fw = Fenwick(5)
    for i, v in enumerate([1, 2, 3, 4, 5], start=1):
        fw.add(i, v)
    print(fw.range_sum(2, 4))


if __name__ == "__main__":
    main()
