package main

import "fmt"

func countSubarrayLeK(xs []int, k int) int {
	n := len(xs)
	ans, left, sum := 0, 0, 0
	for right := 0; right < n; right++ {
		sum += xs[right]
		for sum > k && left <= right {
			sum -= xs[left]
			left++
		}
		ans += right - left + 1
	}
	return ans
}

func main() {
	fmt.Println(countSubarrayLeK([]int{1, 2, 3, 4}, 5))
}
