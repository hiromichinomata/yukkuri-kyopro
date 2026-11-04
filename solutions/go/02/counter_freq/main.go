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
		if pairs[i].v != pairs[j].v {
			return pairs[i].v > pairs[j].v // 多い順
		}
		return pairs[i].k < pairs[j].k
	})
	for _, p := range pairs[:2] {
		fmt.Println(p.k, p.v)
	}
}
