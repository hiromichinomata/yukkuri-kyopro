package main

import (
	"fmt"
	"sort"
)

func subsetSums(xs []int) []int {
	sums := []int{0}
	for _, x := range xs {
		next := make([]int, 0, len(sums)*2)
		for _, s := range sums {
			next = append(next, s+x)
		}
		sums = append(next, sums...)
	}
	return sums
}

func canMakeSum(xs []int, target int) bool {
	n := len(xs)
	mid := n / 2
	left := subsetSums(xs[:mid])
	sort.Ints(left)
	right := subsetSums(xs[mid:])
	for _, s := range right {
		need := target - s
		i := sort.SearchInts(left, need)
		if i < len(left) && left[i] == need {
			return true
		}
	}
	return false
}

func main() {
	xs := []int{1, 2, 4, 8, 16}
	for _, t := range []int{0, 7, 15, 31, 32} {
		fmt.Println(t, canMakeSum(xs, t))
	}
}
