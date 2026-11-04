package main

import (
	"bufio"
	"fmt"
	"os"
)

// firstInRange は (a*x mod m) が lo 以上 hi 以下になる最小の x ≥ 0（0 ≤ lo ≤ hi < m）。なければ -1。
// ユークリッドの互除法と同じ形で (a, m) → (m mod a, a) と小さくしていくので O(log m)
func firstInRange(a, m, lo, hi int) int {
	if lo == 0 {
		return 0
	}
	a %= m
	if a == 0 {
		return -1
	}
	x := (lo + a - 1) / a // 折り返さずに届く最小の x
	if a*x <= hi {
		return x
	}
	// a*x = m*y + (lo〜hi) となる最小の y を探す。⇔ (m*y mod a) が (-hi mod a)〜(-lo mod a) にある
	y := firstInRange(m%a, a, ((-hi)%a+a)%a, ((-lo)%a+a)%a)
	if y == -1 {
		return -1
	}
	return (m*y + lo + a - 1) / a
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func solve(n, a, b int) (int, int) {
	g := gcd(a, b)
	// L = a*l + 1, R = a*r - 1, k = r - l。長さ k・ずれ t で作れる
	// ⇔ (k-1) - floor((a*k - 1 + b - t) / b) ≤ n ⇔ t ≤ a*k - 1 + b - b*(k-1-n)
	k := (b*(n+2) - 1 - g) / (b - a)
	c := min(b, a*k-1+b-b*(k-1-n)) // この k で許される t の上限
	l := 0
	if c < b {
		l = firstInRange(a, b, b-c, b-1) // (a*l mod b) ≥ b - c となる最小の l
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
