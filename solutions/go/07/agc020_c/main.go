package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

// orShift は b |= b << s（b は uint64 を並べた bitset）
func orShift(b []uint64, s int) {
	ws, bs := s/64, uint(s%64)
	for i := len(b) - 1; i >= ws; i-- {
		v := b[i-ws] << bs
		if bs > 0 && i-ws-1 >= 0 {
			v |= b[i-ws-1] >> (64 - bs)
		}
		b[i] |= v
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	a := make([]int, n)
	total := 0
	for i := range a {
		fmt.Fscan(in, &a[i])
		total += a[i]
	}
	// i ビット目が 1 ⇔ 部分和 i が作れる
	b := make([]uint64, total/64+1)
	b[0] = 1
	for _, x := range a {
		orShift(b, x)
	}
	// 部分和 s と total - s は 1 対 1 に対応するので、total / 2 以上の最小の部分和が答え
	for v := (total + 1) / 2; v <= total; v++ {
		w := b[v/64] >> uint(v%64)
		if w != 0 {
			fmt.Fprintln(out, v+bits.TrailingZeros64(w))
			return
		}
		v += 63 - v%64 // この 64 ビットの塊には 1 がない → 次の塊へ
	}
}
