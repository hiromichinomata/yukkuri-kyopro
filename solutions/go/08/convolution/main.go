package main

import "fmt"

const mod = 998244353
const g = 3

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

func ntt(a []int, invert bool) {
	n := len(a)
	j := 0
	for i := 1; i < n; i++ {
		bit := n >> 1
		for j&bit != 0 {
			j ^= bit
			bit >>= 1
		}
		j ^= bit
		if i < j {
			a[i], a[j] = a[j], a[i]
		}
	}
	for length := 2; length <= n; length <<= 1 {
		w := powMod(g, (mod-1)/length)
		if invert {
			w = powMod(w, mod-2)
		}
		for i := 0; i < n; i += length {
			wn := 1
			for k := 0; k < length/2; k++ {
				u := a[i+k]
				v := a[i+k+length/2] * wn % mod
				a[i+k] = (u + v) % mod
				a[i+k+length/2] = (u - v + mod) % mod
				wn = wn * w % mod
			}
		}
	}
	if invert {
		invN := powMod(n, mod-2)
		for i := range a {
			a[i] = a[i] * invN % mod
		}
	}
}

func conv(a, b []int) []int {
	need := 1
	for need < len(a)+len(b)-1 {
		need <<= 1
	}
	fa := make([]int, need)
	fb := make([]int, need)
	copy(fa, a)
	copy(fb, b)
	ntt(fa, false)
	ntt(fb, false)
	for i := 0; i < need; i++ {
		fa[i] = fa[i] * fb[i] % mod
	}
	ntt(fa, true)
	return fa[:len(a)+len(b)-1]
}

func main() {
	fmt.Println(conv([]int{1, 2, 3}, []int{4, 5}))
}
