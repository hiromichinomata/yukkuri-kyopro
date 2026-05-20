package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &a[i])
	}
	sort.Ints(a)
	const k = 2
	total := 0
	for i, price := range a {
		remaining := n - i
		if remaining%k == 0 {
			total += price / 2
		} else {
			total += price
		}
	}
	fmt.Println(total)
}
