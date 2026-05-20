package main

import "fmt"

const mod = 998244353
const g = 3

func pow(a, e int) int {
	res := 1
	for e > 0 {
		if e&1 == 1 {
			res = res * a % mod
		}
		a = a * a % mod
		e >>= 1
	}
	return res
}

func ntt(a []int, invert bool) []int {
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
		w := pow(g, (mod-1)/length)
		if invert {
			w = pow(w, mod-2)
		}
		for i := 0; i < n; i += length {
			half := length / 2
			for j := 0; j < half; j++ {
				u := a[i+j]
				v := a[i+j+half] * w % mod
				a[i+j] = (u + v) % mod
				a[i+j+half] = (u - v + mod) % mod
			}
		}
	}
	if invert {
		invN := pow(n, mod-2)
		for i := range a {
			a[i] = a[i] * invN % mod
		}
	}
	return a
}

func convolution(a, b []int) []int {
	n1, n2 := len(a), len(b)
	n := 1
	for n < n1+n2-1 {
		n <<= 1
	}
	fa := make([]int, n)
	fb := make([]int, n)
	copy(fa, a)
	copy(fb, b)
	fa = ntt(fa, false)
	fb = ntt(fb, false)
	for i := 0; i < n; i++ {
		fa[i] = fa[i] * fb[i] % mod
	}
	fa = ntt(fa, true)
	return fa[:n1+n2-1]
}

func main() {
	fmt.Println(convolution([]int{1, 1}, []int{1, 1}))
}
