from collections import deque


def cht_min(lines):
    """傾き単調増加の直線 y = m*x + b の下包絡（クエリ x 単調増）"""
    dq = deque()

    def bad(l1, l2, l3):
        return (l2[1] - l1[1]) * (l3[0] - l2[0]) >= (l2[0] - l1[0]) * (l3[1] - l2[1])

    for ln in lines:
        while len(dq) >= 2 and bad(dq[-2], dq[-1], ln):
            dq.pop()
        dq.append(ln)
    return dq


def query(dq, x):
    while len(dq) >= 2:
        m1, b1 = dq[0]
        m2, b2 = dq[1]
        if m1 * x + b1 <= m2 * x + b2:
            break
        dq.popleft()
    m, b = dq[0]
    return m * x + b


def main() -> None:
    lines = [(1, 0), (2, -1), (3, -5)]
    dq = cht_min(lines)
    print(query(dq, 0), query(dq, 1), query(dq, 2))


if __name__ == "__main__":
    main()
