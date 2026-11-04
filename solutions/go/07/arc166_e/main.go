package main

import (
	"bufio"
	"fmt"
	"os"
)

// floorSum は sum_{i=0}^{n-1} floor((a*i + b) / m)（AtCoder Library と同じ計算）
func floorSum(n, m, a, b int) int {
	ans := 0
	for {
		if a >= m {
			ans += (n - 1) * n / 2 * (a / m)
			a %= m
		}
		if b >= m {
			ans += n * (b / m)
			b %= m
		}
		yMax := a*n + b
		if yMax < m {
			return ans
		}
		n, b, m, a = yMax/m, yMax%m, a, m
	}
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func solve(n, a, b int) (int, int) {
	g := gcd(a, b)
	// L = a*l + 1, R = a*r - 1, k = r - l。長さ k が作れる ⇔ f(k, g) ≤ n（f は k について単調）
	f := func(k, t int) int { return (k - 1) - (a*k-1+b-t)/b }
	lo, hi := 1, 1
	for f(hi, g) <= n {
		hi *= 2
	}
	for hi-lo > 1 {
		mid := (lo + hi) / 2
		if f(mid, g) <= n {
			lo = mid
		} else {
			hi = mid
		}
	}
	k := lo
	tl, th := g, b+1 // 条件を満たす t の上限 c
	for th-tl > 1 {
		mid := (tl + th) / 2
		if f(k, mid) <= n {
			tl = mid
		} else {
			th = mid
		}
	}
	c := tl
	l := 0
	if c < b {
		// (a*x mod b) ≥ b - c となる最小の x ≥ 1（個数を floor_sum で数えて二分探索）
		count := func(x int) int { return floorSum(x+1, b, a, c) - floorSum(x+1, b, a, 0) }
		lo2, hi2 := 0, b
		for hi2-lo2 > 1 {
			mid := (lo2 + hi2) / 2
			if count(mid) >= 1 {
				hi2 = mid
			} else {
				lo2 = mid
			}
		}
		l = hi2
	}
	return a*l + 1, a*(l+k) - 1
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var n, a, b int
		fmt.Fscan(in, &n, &a, &b)
		L, R := solve(n, a, b)
		fmt.Fprintln(out, L, R)
	}
}
