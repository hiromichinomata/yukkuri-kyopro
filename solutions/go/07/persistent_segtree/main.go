package main

import "fmt"

type node struct {
	l, r *node
	val  int
}

func clone(n *node) *node {
	if n == nil {
		return nil
	}
	return &node{l: n.l, r: n.r, val: n.val}
}

func build(l, r int, arr []int) *node {
	if l == r {
		return &node{val: arr[l]}
	}
	mid := (l + r) / 2
	n := &node{}
	n.l = build(l, mid, arr)
	n.r = build(mid+1, r, arr)
	n.val = n.l.val + n.r.val
	return n
}

func update(n *node, l, r, idx, delta int) *node {
	n = clone(n)
	if l == r {
		n.val += delta
		return n
	}
	mid := (l + r) / 2
	if idx <= mid {
		n.l = update(n.l, l, mid, idx, delta)
	} else {
		n.r = update(n.r, mid+1, r, idx, delta)
	}
	n.val = val(n.l) + val(n.r)
	return n
}

func val(n *node) int {
	if n == nil {
		return 0
	}
	return n.val
}

func query(n *node, l, r, ql, qr int) int {
	if n == nil || qr < l || r < ql {
		return 0
	}
	if ql <= l && r <= qr {
		return n.val
	}
	mid := (l + r) / 2
	return query(n.l, l, mid, ql, qr) + query(n.r, mid+1, r, ql, qr)
}

func main() {
	arr := []int{1, 2, 3, 4, 5}
	n := len(arr)
	r0 := build(0, n-1, arr)
	r1 := update(r0, 0, n-1, 2, 10)
	fmt.Println(query(r0, 0, n-1, 0, n-1))
	fmt.Println(query(r1, 0, n-1, 0, n-1))
}
