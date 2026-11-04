package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type rule struct{ t, w, s int } // A_u ≥ t ならば A_w ≥ s

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, k int
	fmt.Fscan(in, &n, &m, &k)
	// 条件 i は「A_P ≥ X ⇔ A_Q ≥ Y」かつ「A_P ≥ X+1 ⇔ A_Q ≥ Y+1」と同じ
	rules := make([][]rule, n)
	for i := 0; i < k; i++ {
		var p, x, q, y int
		fmt.Fscan(in, &p, &x, &q, &y) // 入力は P X Q Y の順
		p--
		q--
		rules[p] = append(rules[p], rule{x, q, y}, rule{x + 1, q, y + 1})
		rules[q] = append(rules[q], rule{y, p, x}, rule{y + 1, p, x + 1})
	}
	for _, r := range rules {
		sort.Slice(r, func(i, j int) bool { return r[i].t < r[j].t })
	}
	a := make([]int, n) // すべて 1 から始め、必要な分だけ値を上げていく
	for i := range a {
		a[i] = 1
	}
	ptr := make([]int, n)
	q := make([]int, 0, n)
	for i := 0; i < n; i++ {
		q = append(q, i)
	}
	for head := 0; head < len(q); head++ {
		u := q[head]
		r := rules[u]
		for ptr[u] < len(r) && r[ptr[u]].t <= a[u] {
			w, s := r[ptr[u]].w, r[ptr[u]].s
			ptr[u]++
			if a[w] < s {
				a[w] = s
				if s > m { // M を超えたら満たす数列はない
					fmt.Println(-1)
					return
				}
				q = append(q, w)
			}
		}
	}
	sum := 0
	for _, v := range a {
		sum += v
	}
	fmt.Println(sum)
}
