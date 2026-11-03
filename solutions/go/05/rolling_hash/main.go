package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"math/rand"
	"os"
)

const hashMod = (1 << 61) - 1

// mulMod は a*b mod (2^61-1) を 128 ビットの積で計算する。
func mulMod(a, b uint64) uint64 {
	hi, lo := bits.Mul64(a, b)
	// 積 = hi*2^64 + lo。2^61 ≡ 1 なので、上位と下位 61 ビットを足せばよい
	res := (hi<<3 | lo>>61) + (lo & hashMod)
	if res >= hashMod {
		res -= hashMod
	}
	return res
}

type rollingHash struct {
	h, pw []uint64
}

func newRollingHash(s string, base uint64) *rollingHash {
	n := len(s)
	rh := &rollingHash{h: make([]uint64, n+1), pw: make([]uint64, n+1)}
	rh.pw[0] = 1
	for i := 0; i < n; i++ {
		rh.h[i+1] = (mulMod(rh.h[i], base) + uint64(s[i])) % hashMod
		rh.pw[i+1] = mulMod(rh.pw[i], base)
	}
	return rh
}

// get は s[l:r] のハッシュを O(1) で返す。
func (rh *rollingHash) get(l, r int) uint64 {
	return (rh.h[r] + hashMod - mulMod(rh.h[l], rh.pw[r-l])) % hashMod
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var t, p string
	fmt.Fscan(in, &t, &p)
	base := uint64(rand.Int63n(hashMod-100000) + 100000) // 基数はランダムに選ぶ
	ht, hp := newRollingHash(t, base), newRollingHash(p, base)
	count := 0
	if len(p) <= len(t) {
		target := hp.get(0, len(p))
		for i := 0; i+len(p) <= len(t); i++ {
			if ht.get(i, i+len(p)) == target {
				count++
			}
		}
	}
	fmt.Fprintln(out, count)
	// t[0:3] と t[7:10] が等しいかを O(1) で比べる
	if ht.get(0, 3) == ht.get(7, 10) {
		fmt.Fprintln(out, "Yes")
	} else {
		fmt.Fprintln(out, "No")
	}
}
