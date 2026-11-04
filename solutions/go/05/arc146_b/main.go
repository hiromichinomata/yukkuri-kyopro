package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"sort"
)

// cost: a 以上で、target の 1 のビットをすべて持つ最小の数にするのに必要な +1 の回数
func cost(a, target int) int {
	if a&target == target {
		return 0
	}
	// target にあって a にない、いちばん上のビット h
	h := bits.Len(uint(target&^a)) - 1
	// h より上は a のまま、h を立て、h より下は target の分だけにする
	upper := (a >> (h + 1)) << (h + 1)
	x := upper | 1<<h | (target & (1<<h - 1))
	return x - a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m, k int
	fmt.Fscan(in, &n, &m, &k)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	ans := 0
	costs := make([]int, n)
	for b := 30; b >= 0; b-- { // 上のビットから「立てられるか」を貪欲に決める
		cand := ans | 1<<b
		for i, x := range a {
			costs[i] = cost(x, cand)
		}
		sort.Ints(costs)
		sum := 0
		for _, c := range costs[:k] { // 安い K 個に操作を集中させる
			sum += c
		}
		if sum <= m {
			ans = cand
		}
	}
	fmt.Fprintln(out, ans)
}
