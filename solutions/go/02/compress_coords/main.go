package main

import (
	"fmt"
	"sort"
)

func main() {
	values := []int{1_000_000_000, 5, 1_000_000_000, 7, 5}
	uniqSet := map[int]struct{}{}
	for _, v := range values {
		uniqSet[v] = struct{}{}
	}
	uniq := make([]int, 0, len(uniqSet))
	for v := range uniqSet {
		uniq = append(uniq, v)
	}
	sort.Ints(uniq)
	compressed := make([]int, len(values))
	for i, v := range values {
		compressed[i] = sort.SearchInts(uniq, v)
	}
	fmt.Println(uniq)
	fmt.Println(compressed)
}
