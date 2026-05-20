package main

import (
	"bufio"
	"fmt"
	"os"
)

var a []int
var memo [][]int

const unset = 1 << 30

func advantage(l, r int) int {
	if l == r {
		return a[l]
	}
	if memo[l][r] != unset {
		return memo[l][r]
	}
	v1 := a[l] - advantage(l+1, r)
	v2 := a[r] - advantage(l, r-1)
	if v1 > v2 {
		memo[l][r] = v1
	} else {
		memo[l][r] = v2
	}
	return memo[l][r]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	a = make([]int, n)
	total := 0
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &a[i])
		total += a[i]
	}
	memo = make([][]int, n)
	for i := range memo {
		memo[i] = make([]int, n)
		for j := range memo[i] {
			memo[i][j] = unset
		}
	}
	adv := advantage(0, n-1)
	fmt.Println((total + adv) / 2)
}
