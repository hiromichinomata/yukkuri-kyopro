class Node:
    __slots__ = ("l", "r", "val")

    def __init__(self, val=0):
        self.l = self.r = None
        self.val = val


def clone(node):
    if node is None:
        return None
    n = Node(node.val)
    n.l = node.l
    n.r = node.r
    return n


def build(l, r, arr):
    if l == r:
        return Node(arr[l])
    mid = (l + r) // 2
    node = Node()
    node.l = build(l, mid, arr)
    node.r = build(mid + 1, r, arr)
    node.val = node.l.val + node.r.val
    return node


def update(node, l, r, idx, delta):
    node = clone(node)
    if l == r:
        node.val += delta
        return node
    mid = (l + r) // 2
    if idx <= mid:
        node.l = update(node.l, l, mid, idx, delta)
    else:
        node.r = update(node.r, mid + 1, r, idx, delta)
    node.val = (node.l.val if node.l else 0) + (node.r.val if node.r else 0)
    return node


def query(node, l, r, ql, qr):
    if node is None or qr < l or r < ql:
        return 0
    if ql <= l and r <= qr:
        return node.val
    mid = (l + r) // 2
    return query(node.l, l, mid, ql, qr) + query(node.r, mid + 1, r, ql, qr)


def main() -> None:
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    roots = [build(0, n - 1, arr)]
    roots.append(update(roots[0], 0, n - 1, 2, 10))
    print(query(roots[0], 0, n - 1, 0, 4))
    print(query(roots[1], 0, n - 1, 0, 4))


if __name__ == "__main__":
    main()
