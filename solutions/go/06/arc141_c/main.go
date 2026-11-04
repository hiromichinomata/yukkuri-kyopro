package main

import (
	"bufio"
	"fmt"
	"os"
)

// greedy は S から、S_p が正しい括弧列になる順列 p のうち辞書順最小（largest なら最大）を作る。
// 残高が 0 のときは「(」しか取れない。それ以外は使っていない添字の最小（最大）を取ればよい
func greedy(s []byte, largest bool) []int {
	n2 := len(s)
	all := make([]int, 0, n2) // 添字の候補を、取りたい順に並べたもの
	for k := 0; k < n2; k++ {
		if largest {
			all = append(all, n2-1-k)
		} else {
			all = append(all, k)
		}
	}
	var opens []int
	for _, i := range all {
		if s[i] == '(' {
			opens = append(opens, i)
		}
	}
	used := make([]bool, n2)
	pa, po, bal := 0, 0, 0
	res := make([]int, 0, n2)
	for k := 0; k < n2; k++ {
		var i int
		if bal == 0 {
			for used[opens[po]] {
				po++
			}
			i = opens[po]
		} else {
			for used[all[pa]] {
				pa++
			}
			i = all[pa]
		}
		used[i] = true
		if s[i] == '(' {
			bal++
		} else {
			bal--
		}
		res = append(res, i+1)
	}
	return res
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
	p, q := make([]int, 2*n), make([]int, 2*n)
	for i := range p {
		fmt.Fscan(in, &p[i])
	}
	for i := range q {
		fmt.Fscan(in, &q[i])
	}
	s := make([]byte, 2*n)
	ok := true
	force := func(i int, c byte) {
		if s[i] != 0 && s[i] != c {
			ok = false
		}
		s[i] = c
	}
	for k := 0; k < 2*n; k += 2 {
		// 最小の P で「大きい添字 → 小さい添字」なら「(」→「)」、最大の Q では逆に「小 → 大」のとき
		if p[k] > p[k+1] {
			force(p[k]-1, '(')
			force(p[k+1]-1, ')')
		}
		if q[k] < q[k+1] {
			force(q[k]-1, '(')
			force(q[k+1]-1, ')')
		}
	}
	opens := 0
	for _, c := range s {
		if c == 0 {
			ok = false
		}
		if c == '(' {
			opens++
		}
	}
	// 決めた S から最小・最大の順列を作り直し、入力と一致するか確かめる
	if !ok || opens != n || !equal(greedy(s, false), p) || !equal(greedy(s, true), q) {
		fmt.Println(-1)
		return
	}
	fmt.Println(string(s))
}
