package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	a := []int{1, 2, 1, 3, 2, 1, 2}
	queries := [][2]int{{0, 6}, {2, 5}, {1, 4}}
	n := len(a)
	block := int(math.Sqrt(float64(n))) + 1
	type item struct {
		bid, r, l, idx int
	}
	items := make([]item, len(queries))
	for i, q := range queries {
		bid := q[0] / block
		r := q[1]
		if bid%2 == 1 {
			r = -r
		}
		items[i] = item{bid, r, q[0], i}
	}
	sort.Slice(items, func(i, j int) bool {
		if items[i].bid != items[j].bid {
			return items[i].bid < items[j].bid
		}
		return items[i].r < items[j].r
	})
	cnt := map[int]int{}
	curL, curR := 0, 0
	distinct := 0
	ans := make([]int, len(queries))
	add := func(i int) {
		x := a[i]
		cnt[x]++
		if cnt[x] == 1 {
			distinct++
		}
	}
	remove := func(i int) {
		x := a[i]
		cnt[x]--
		if cnt[x] == 0 {
			distinct--
		}
	}
	for _, it := range items {
		l, r := it.l, queries[it.idx][1]
		for curR <= r {
			add(curR)
			curR++
		}
		for curR-1 > r {
			curR--
			remove(curR)
		}
		for curL > l {
			curL--
			add(curL)
		}
		for curL < l {
			remove(curL)
			curL++
		}
		ans[it.idx] = distinct
	}
	fmt.Println(ans)
}
