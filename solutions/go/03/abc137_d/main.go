package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

// MaxHeap は int の最大ヒープ
type MaxHeap []int

func (h MaxHeap) Len() int            { return len(h) }
func (h MaxHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MaxHeap) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n, &m)
	jobs := make([][]int, m+1) // jobs[a]: 報酬まで a 日かかる仕事の報酬
	for i := 0; i < n; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		if a <= m {
			jobs[a] = append(jobs[a], b)
		}
	}
	// 残り r 日の日には「a ≤ r の仕事」が候補になり、その中で最大を取る
	h := &MaxHeap{}
	total := 0
	for r := 1; r <= m; r++ {
		for _, b := range jobs[r] {
			heap.Push(h, b)
		}
		if h.Len() > 0 {
			total += heap.Pop(h).(int)
		}
	}
	fmt.Fprintln(out, total)
}
