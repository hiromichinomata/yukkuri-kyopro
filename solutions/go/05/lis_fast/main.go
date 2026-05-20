package main

import "fmt"

func lowerBound(a []int, x int) int {
	lo, hi := 0, len(a)
	for lo < hi {
		mid := (lo + hi) / 2
		if a[mid] < x {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

func lisLength(a []int) int {
	tails := []int{}
	for _, x := range a {
		i := lowerBound(tails, x)
		if i == len(tails) {
			tails = append(tails, x)
		} else {
			tails[i] = x
		}
	}
	return len(tails)
}

func main() {
	fmt.Println(lisLength([]int{3, 1, 4, 2, 5}))
}
