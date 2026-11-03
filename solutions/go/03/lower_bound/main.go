package main

import (
	"fmt"
	"sort"
)

func lowerBound(a []int, x int) int {
	ng, ok := -1, len(a)
	for ok-ng > 1 {
		mid := (ok + ng) / 2
		if a[mid] >= x {
			ok = mid
		} else {
			ng = mid
		}
	}
	return ok
}

func main() {
	a := []int{1, 3, 3, 5, 7}
	fmt.Println(sort.SearchInts(a, 4), lowerBound(a, 4)) // 標準ライブラリと自作が一致
}
