def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def closest_pair(points):
    points = sorted(points)
    n = len(points)
    if n <= 1:
        return 0

    def solve(l, r):
        if r - l <= 3:
            best = 10**30
            for i in range(l, r):
                for j in range(i + 1, r):
                    best = min(best, dist2(points[i], points[j]))
            return best
        mid = (l + r) // 2
        midx = points[mid][0]
        d = min(solve(l, mid), solve(mid, r))
        strip = [p for p in points[l:r] if (p[0] - midx) ** 2 < d]
        strip.sort(key=lambda p: p[1])
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 8, len(strip))):
                d = min(d, dist2(strip[i], strip[j]))
        return d

    return solve(0, n)


def main() -> None:
    pts = [(0, 0), (1, 1), (3, 4), (0, 5), (2, 2)]
    print(closest_pair(pts) ** 0.5)


if __name__ == "__main__":
    main()
