package main

import "fmt"

func zAlgorithm(s string) []int {
	n := len(s)
	z := make([]int, n)
	l, r := 0, 0
	for i := 1; i < n; i++ {
		if i <= r {
			if z[i-l] < r-i+1 {
				z[i] = z[i-l]
			} else {
				z[i] = r - i + 1
			}
		}
		for i+z[i] < n && s[z[i]] == s[i+z[i]] {
			z[i]++
		}
		if i+z[i]-1 > r {
			l, r = i, i+z[i]-1
		}
	}
	return z
}

func main() {
	fmt.Println(zAlgorithm("aaaaabaa"))
}
