package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// canByCondition は考察で得た条件: 裏（'1'）の枚数が偶数なら全部表にできる。
func canByCondition(s string) bool {
	return strings.Count(s, "1")%2 == 0
}

// canByBFS は小さい N 用の全探索。隣り合う 2 枚を同時に裏返して全部 '0' にできるか。
func canByBFS(s string) bool {
	n := len(s)
	start := 0
	for _, c := range s {
		start = start*2 + int(c-'0')
	}
	seen := map[int]bool{start: true}
	q := []int{start}
	for len(q) > 0 {
		v := q[0]
		q = q[1:]
		if v == 0 {
			return true
		}
		for i := 0; i+1 < n; i++ {
			nv := v ^ (0b11 << i) // 隣り合う 2 ビットを反転
			if !seen[nv] {
				seen[nv] = true
				q = append(q, nv)
			}
		}
	}
	return false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	// 必要十分性の確認: 長さ 1〜10 のすべての並びで、条件と全探索が一致するか
	for n := 1; n <= 10; n++ {
		for mask := 0; mask < 1<<n; mask++ {
			s := fmt.Sprintf("%0*b", n, mask)
			if canByCondition(s) != canByBFS(s) {
				panic(s)
			}
		}
	}
	fmt.Fprintln(out, "condition == bfs for all n <= 10")
	var s string
	fmt.Fscan(in, &s)
	if canByCondition(s) {
		fmt.Fprintln(out, "Yes")
	} else {
		fmt.Fprintln(out, "No")
	}
}
