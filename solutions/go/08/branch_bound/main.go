package main

import "fmt"

func subsetSumPruned(xs []int, target int) bool {
	sortDesc := make([]int, len(xs))
	copy(sortDesc, xs)
	for i := 0; i < len(sortDesc); i++ {
		for j := i + 1; j < len(sortDesc); j++ {
			if sortDesc[j] > sortDesc[i] {
				sortDesc[i], sortDesc[j] = sortDesc[j], sortDesc[i]
			}
		}
	}
	best := false
	var dfs func(i, rem int)
	dfs = func(i, rem int) {
		if rem == 0 {
			best = true
			return
		}
		if rem < 0 || i == len(sortDesc) {
			return
		}
		s := 0
		for j := i; j < len(sortDesc); j++ {
			s += sortDesc[j]
		}
		if s < rem {
			return
		}
		dfs(i+1, rem-sortDesc[i])
		if best {
			return
		}
		dfs(i+1, rem)
	}
	dfs(0, target)
	return best
}

func main() {
	xs := []int{3, 7, 8, 2, 5}
	for _, t := range []int{10, 11, 23, 24} {
		fmt.Println(t, subsetSumPruned(xs, t))
	}
}
