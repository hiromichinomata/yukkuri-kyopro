package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var s string
	fmt.Fscan(in, &s)
	cnt := 0
	for _, ch := range s {
		if ch != '0' {
			cnt++
		}
	}
	fmt.Println(cnt)
}
