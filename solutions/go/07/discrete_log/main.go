package main

import (
	"fmt"
	"math"
)

func bsgs(a, b, p, m int) int {
	a %= p
	b %= p
	step := int(math.Sqrt(float64(m))) + 1
	baby := map[int]int{1: 0}
	cur := 1
	for j := 1; j <= step; j++ {
		cur = cur * a % p
		if _, ok := baby[cur]; !ok {
			baby[cur] = j
		}
	}
	factor := powMod(a, step*(p-2), p)
	gamma := b
	for i := 0; i <= step; i++ {
		if j, ok := baby[gamma]; ok {
			return i*step + j
		}
		gamma = gamma * factor % p
	}
	return -1
}

func powMod(a, e, p int) int {
	res := 1
	a %= p
	for e > 0 {
		if e&1 == 1 {
			res = res * a % p
		}
		a = a * a % p
		e >>= 1
	}
	return res
}

func main() {
	p := 1_000_000_009
	fmt.Println(bsgs(2, 8, p, p-1))
}
