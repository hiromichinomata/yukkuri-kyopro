package main

import (
	"fmt"
	"sort"
)

func main() {
	xs := []int{1, 2, 2, 3, 3, 3}
	freq := map[int]int{}
	for _, x := range xs {
		freq[x]++
	}
	fmt.Println(freq[2])
	type kv struct {
		k, v int
	}
	var pairs []kv
	for k, v := range freq {
		pairs = append(pairs, kv{k, v})
	}
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].v > pairs[j].v
	})
	if len(pairs) >= 2 {
		fmt.Println(pairs[:2])
	}
}
