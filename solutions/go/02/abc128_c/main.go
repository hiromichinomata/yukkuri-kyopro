package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	bulbs := make([][]int, m)
	for i := range bulbs {
		var k int
		fmt.Fscan(in, &k)
		bulbs[i] = make([]int, k)
		for j := range bulbs[i] {
			fmt.Fscan(in, &bulbs[i][j])
			bulbs[i][j]--
		}
	}
	p := make([]int, m)
	for i := range p {
		fmt.Fscan(in, &p[i])
	}
	ans := 0
	for mask := 0; mask < 1<<n; mask++ { // スイッチの on / off を 2^N 通り全部試す
		ok := true
		for i, b := range bulbs {
			on := 0
			for _, s := range b {
				on += mask >> s & 1
			}
			if on%2 != p[i] {
				ok = false
				break
			}
		}
		if ok {
			ans++
		}
	}
	fmt.Println(ans)
}
