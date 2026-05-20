package main

import (
	"fmt"
	"sort"
)

type pair struct{ a, b int }

func main() {
	ps := []pair{{1, 3}, {2, 1}, {4, 2}}
	sort.Slice(ps, func(i, j int) bool {
		return ps[i].b < ps[j].b
	})
	fmt.Println(ps)
}
