package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxV = 100000

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	// エラトステネスの篩
	isPrime := make([]bool, maxV+1)
	for i := 2; i <= maxV; i++ {
		isPrime[i] = true
	}
	for i := 2; i*i <= maxV; i++ {
		if isPrime[i] {
			for j := i * i; j <= maxV; j += i {
				isPrime[j] = false
			}
		}
	}
	// cnt[x]: x 以下の「2017 に似た数」の個数（累積和）
	cnt := make([]int, maxV+1)
	for x := 1; x <= maxV; x++ {
		cnt[x] = cnt[x-1]
		if x%2 == 1 && isPrime[x] && isPrime[(x+1)/2] {
			cnt[x]++
		}
	}
	var q int
	fmt.Fscan(in, &q)
	for ; q > 0; q-- {
		var l, r int
		fmt.Fscan(in, &l, &r)
		fmt.Fprintln(out, cnt[r]-cnt[l-1])
	}
}
