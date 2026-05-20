package main

import "fmt"

func maxSumK(xs []int, k int) int {
	s, ans := 0, -1<<60
	left := 0
	for right, x := range xs {
		s += x
		if right-left+1 > k {
			s -= xs[left]
			left++
		}
		if right-left+1 == k {
			if s > ans {
				ans = s
			}
		}
	}
	return ans
}

func main() {
	xs := []int{1, 2, 3, 4, 5}
	fmt.Println(maxSumK(xs, 3))
}
