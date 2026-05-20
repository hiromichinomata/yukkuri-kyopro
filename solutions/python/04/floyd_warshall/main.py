def floyd(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < 10**17 and dist[k][j] < 10**17:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def main() -> None:
    INF = 10**17
    dist = [
        [0, 3, INF],
        [INF, 0, 1],
        [2, INF, 0],
    ]
    print(floyd(dist))


if __name__ == "__main__":
    main()
