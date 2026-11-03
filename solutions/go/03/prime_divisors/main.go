package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i*i <= n; i++ { // √n まで割ってみれば十分
		if n%i == 0 {
			return false
		}
	}
	return true
}

func divisors(n int) []int {
	small, large := []int{}, []int{}
	for i := 1; i*i <= n; i++ {
		if n%i == 0 {
			small = append(small, i)
			if i != n/i { // 平方数で同じ約数を 2 回入れない
				large = append(large, n/i)
			}
		}
	}
	for i := len(large) - 1; i >= 0; i-- { // 昇順にする
		small = append(small, large[i])
	}
	return small
}

type factor struct{ p, e int }

func factorize(n int) []factor {
	res := []factor{}
	for p := 2; p*p <= n; p++ {
		if n%p == 0 {
			e := 0
			for n%p == 0 {
				n /= p
				e++
			}
			res = append(res, factor{p, e})
		}
	}
	if n > 1 { // 残りは √n より大きい素数
		res = append(res, factor{n, 1})
	}
	return res
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	if isPrime(n) {
		fmt.Fprintln(out, "Yes")
	} else {
		fmt.Fprintln(out, "No")
	}
	ds := []string{}
	for _, d := range divisors(n) {
		ds = append(ds, fmt.Sprint(d))
	}
	fmt.Fprintln(out, strings.Join(ds, " "))
	fs := []string{}
	for _, f := range factorize(n) {
		fs = append(fs, fmt.Sprintf("%d^%d", f.p, f.e))
	}
	fmt.Fprintln(out, strings.Join(fs, " "))
}
