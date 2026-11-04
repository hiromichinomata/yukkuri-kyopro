package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(a))) // 大きい順に並べる
	diff := 0                                 // Alice の得点 - Bob の得点
	turn := 0                                 // 0: Alice, 1: Bob
	for _, x := range a {
		if turn == 0 {
			diff += x
		} else {
			diff -= x
		}
		turn ^= 1
	}
	fmt.Fprintln(out, diff)
}
