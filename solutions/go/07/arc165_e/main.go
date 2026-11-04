package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 998244353

func powMod(a, e int) int {
	res := 1
	a %= mod
	for e > 0 {
		if e&1 == 1 {
			res = res * a % mod
		}
		a = a * a % mod
		e >>= 1
	}
	return res
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	g := make([][]int, n)
	for i := 0; i < n-1; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		g[a-1] = append(g[a-1], b-1)
		g[b-1] = append(g[b-1], a-1)
	}
	fac := make([]int, 2*n+2)
	fac[0] = 1
	for i := 1; i < len(fac); i++ {
		fac[i] = fac[i-1] * i % mod
	}
	// v が選ばれる確率 = Σ_{連結な S ∋ v, |S| = s ≥ K+1} b!(s-1)!/(s+b)!（b は S に隣接する外の頂点数）。
	// S ごとに v の選び方が s 通りあるので、連結な S を (s, b) ごとに数える（木 DP）
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -2
	}
	parent[0] = -1
	order := []int{0}
	for h := 0; h < len(order); h++ {
		v := order[h]
		for _, to := range g[v] {
			if parent[to] == -2 {
				parent[to] = v
				order = append(order, to)
			}
		}
	}
	// dp[v][s][b]: v を一番上とする連結な S（v の部分木内）で、大きさ s、部分木内の境界 b
	dp := make([][][]int, n)
	size := make([]int, n)
	total := 0
	for idx := n - 1; idx >= 0; idx-- {
		v := order[idx]
		size[v] = 1
		cur := [][]int{nil, {1}} // cur[s][b]
		for _, c := range g[v] {
			if c == parent[v] {
				continue
			}
			ns := size[v] + size[c]
			nxt := make([][]int, ns+1)
			for s := range nxt {
				nxt[s] = make([]int, ns+2)
			}
			for s1 := 1; s1 < len(cur); s1++ {
				for b1, x := range cur[s1] {
					if x == 0 {
						continue
					}
					nxt[s1][b1+1] = (nxt[s1][b1+1] + x) % mod // 子 c を S に入れない → c は境界
					for s2 := 1; s2 < len(dp[c]); s2++ {
						for b2, y := range dp[c][s2] {
							if y != 0 {
								nxt[s1+s2][b1+b2] = (nxt[s1+s2][b1+b2] + x*y) % mod
							}
						}
					}
				}
			}
			size[v] = ns
			cur = nxt
			dp[c] = nil
		}
		dp[v] = cur
		extra := 0
		if parent[v] != -1 {
			extra = 1 // 親も境界
		}
		for s := k + 1; s < len(cur); s++ {
			for b, x := range cur[s] {
				if x == 0 {
					continue
				}
				bb := b + extra
				p := fac[bb] * fac[s-1] % mod * powMod(fac[s+bb], mod-2) % mod
				total = (total + x*s%mod*p) % mod
			}
		}
	}
	fmt.Println(total)
}
