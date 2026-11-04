from collections import deque


def cht_min(lines):
    """y = m*x + b の下包絡（最小値）を作る。

    前提: lines は傾き m の **降順**（単調減少）、クエリ x は **昇順**。
    同じ傾きの直線は切片 b が小さい方だけ残す。
    """
    dq = deque()

    def bad(l1, l2, l3):
        # l1, l3 の交点が l1, l2 の交点より左（以下）なら l2 は最小にならない
        return (l3[1] - l1[1]) * (l1[0] - l2[0]) <= (l2[1] - l1[1]) * (l1[0] - l3[0])

    for ln in lines:
        if dq and dq[-1][0] == ln[0]:
            if dq[-1][1] <= ln[1]:
                continue
            dq.pop()
        while len(dq) >= 2 and bad(dq[-2], dq[-1], ln):
            dq.pop()
        dq.append(ln)
    return dq


def query(dq, x):
    """x は前回のクエリ以上であること（先頭の直線を捨てていくため）"""
    while len(dq) >= 2:
        m1, b1 = dq[0]
        m2, b2 = dq[1]
        if m1 * x + b1 < m2 * x + b2:
            break
        dq.popleft()
    m, b = dq[0]
    return m * x + b


def main() -> None:
    lines = [(3, -5), (2, -1), (1, 0)]  # 傾き降順
    dq = cht_min(lines)
    print(query(dq, 0), query(dq, 1), query(dq, 2))


if __name__ == "__main__":
    main()
