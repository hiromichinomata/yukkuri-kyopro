package main

import "fmt"

func main() {
	n := 5
	diff := make([]int, n+2)
	addRange := func(l, r, v int) {
		diff[l] += v
		diff[r+1] -= v
	}
	addRange(1, 3, 10)
	addRange(2, 5, 5)
	a := make([]int, n+1)
	for i := 1; i <= n; i++ {
		a[i] = a[i-1] + diff[i]
	}
	fmt.Println(a[1:])
}
