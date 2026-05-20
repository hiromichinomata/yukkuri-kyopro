package main

import (
	"fmt"
	"sort"
)

func kth(arr []int, l, r, k int) int {
	sub := make([]int, r-l)
	copy(sub, arr[l:r])
	sort.Ints(sub)
	return sub[k]
}

func main() {
	arr := []int{3, 1, 4, 1, 5, 9, 2, 6}
	fmt.Println(kth(arr, 0, 8, 3))
	fmt.Println(kth(arr, 2, 6, 1))
}
