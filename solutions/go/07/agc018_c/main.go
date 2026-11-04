package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"sort"
)

// MinHeap は int の最小ヒープ
type MinHeap []int

func (h MinHeap) Len() int            { return len(h) }
func (h MinHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

// topSums は、先頭から順に値を見て「大きい k 個の和」を記録する（k 個そろうまでは -1）
func topSums(vals []int, k int) []int {
	res := make([]int, len(vals)+1)
	res[0] = -1
	h := &MinHeap{}
	s := 0
	for i, v := range vals {
		heap.Push(h, v)
		s += v
		if h.Len() > k {
			s -= heap.Pop(h).(int)
		}
		if h.Len() == k {
			res[i+1] = s
		} else {
			res[i+1] = -1
		}
	}
	return res
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var x, y, z int
	fmt.Fscan(in, &x, &y, &z)
	n := x + y + z
	type person struct{ b, c int }
	ps := make([]person, n)
	base := 0
	for i := range ps {
		var a, b, c int
		fmt.Fscan(in, &a, &b, &c)
		base += a // いったん全員から金貨をもらったことにする
		ps[i] = person{b - a, c - a}
	}
	// 「銀の得 − 銅の得」が大きい順に並べ、境界 k の前から Y 人を銀、後ろから Z 人を銅に選ぶ
	sort.Slice(ps, func(i, j int) bool { return ps[i].b-ps[i].c > ps[j].b-ps[j].c })
	bs, cs := make([]int, n), make([]int, n)
	for i, p := range ps {
		bs[i] = p.b
		cs[n-1-i] = p.c // 後ろから見るので逆順
	}
	pre := topSums(bs, y)
	suf := topSums(cs, z) // suf[j]: 後ろ j 人から選んだ和
	best := -1 << 62
	for k := y; k <= n-z; k++ {
		if v := pre[k] + suf[n-k]; v > best {
			best = v
		}
	}
	fmt.Println(base + best)
}
