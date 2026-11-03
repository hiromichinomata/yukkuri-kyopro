package main

import (
	"bufio"
	"fmt"
	"os"
)

func nextPermutation(p []int) bool {
	i := len(p) - 2
	for i >= 0 && p[i] >= p[i+1] {
		i--
	}
	if i < 0 {
		return false
	}
	j := len(p) - 1
	for p[j] <= p[i] {
		j--
	}
	p[i], p[j] = p[j], p[i]
	for l, r := i+1, len(p)-1; l < r; l, r = l+1, r-1 {
		p[l], p[r] = p[r], p[l]
	}
	return true
}

func equal(a, b []int) bool {
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	p, q := make([]int, n), make([]int, n)
	for i := range p {
		fmt.Fscan(in, &p[i])
	}
	for i := range q {
		fmt.Fscan(in, &q[i])
	}
	perm := make([]int, n)
	for i := range perm {
		perm[i] = i + 1
	}
	// 辞書順に列挙して、何番目に出てくるかを数える
	a, b := 0, 0
	for k := 0; ; k++ {
		if equal(perm, p) {
			a = k
		}
		if equal(perm, q) {
			b = k
		}
		if !nextPermutation(perm) {
			break
		}
	}
	if a < b {
		a, b = b, a
	}
	fmt.Println(a - b)
}
