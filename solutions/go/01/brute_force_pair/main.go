package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	xs := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &xs[i])
	}
	ok := false
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if xs[i]+xs[j] == k {
				ok = true
				break
			}
		}
		if ok {
			break
		}
	}
	if ok {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
