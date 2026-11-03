package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	a := make([]int, 3)
	fmt.Fscan(in, &a[0], &a[1], &a[2])
	sort.Ints(a) // 並べ替えてよいので、小さい順にして調べる
	if a[2]-a[1] == a[1]-a[0] {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
