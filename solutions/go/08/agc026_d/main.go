package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1_000_000_007

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

// solve は列 l..r の高さ base より上の塗り方: (最下行が交互の塗り方の数, 全体の数)
func solve(h []int, l, r, base int) (int, int) {
	mh := h[l]
	for i := l; i <= r; i++ {
		if h[i] < mh {
			mh = h[i]
		}
	}
	prodAlt, prodSum, free := 1, 1, 0
	for i := l; i <= r; {
		if h[i] == mh {
			free++
			i++
			continue
		}
		j := i
		for j+1 <= r && h[j+1] > mh {
			j++
		}
		a, b := solve(h, i, j, mh)
		prodAlt = prodAlt * a % mod
		prodSum = prodSum * ((a + b) % mod) % mod
		i = j + 1
	}
	// 最上行が交互: 長方形の各行 2 通り × 上の区間も最下行が交互
	alt := powMod(2, mh-base) * prodAlt % mod
	// 最上行が交互でない: 全パターンの和（列ごとに独立）から交互の 2 パターンを引く
	nonAlt := (powMod(2, free)*prodSum%mod - 2*prodAlt%mod + 2*mod) % mod
	return alt, (alt + nonAlt) % mod
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	h := make([]int, n)
	for i := range h {
		fmt.Fscan(in, &h[i])
	}
	_, all := solve(h, 0, n-1, 0)
	fmt.Println(all)
}
