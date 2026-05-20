class XorBasis:
    def __init__(self, bits=60):
        self.b = [0] * bits

    def add(self, x):
        for i in range(len(self.b) - 1, -1, -1):
            if (x >> i) & 1 == 0:
                continue
            if self.b[i] == 0:
                self.b[i] = x
                return True
            x ^= self.b[i]
        return False

    def max_xor(self):
        x = 0
        for i in range(len(self.b) - 1, -1, -1):
            if self.b[i] and (x >> i) & 1 == 0:
                x ^= self.b[i]
        return x


def main() -> None:
    basis = XorBasis()
    for v in [8, 4, 2, 1, 5, 3]:
        basis.add(v)
    print(basis.max_xor())


if __name__ == "__main__":
    main()
