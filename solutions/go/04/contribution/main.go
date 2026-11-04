package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// sumOfAllSubarraySums はすべての連続部分列の和の総和を、a[i] が何個の区間に含まれるかで数える。
func sumOfAllSubarraySums(a []int) int {
	n := len(a)
	total := 0
	for i, x := range a {
		left := i + 1  // 区間の左端の選び方: 0..i
		right := n - i // 区間の右端の選び方: i..n-1
		total += x * left * right
	}
	return total
}

// sumOfPairDiffs は i < j のすべてのペアの |a_i - a_j| の総和を、ソートして寄与で数える。
func sumOfPairDiffs(a []int) int {
	b := append([]int{}, a...)
	sort.Ints(b)
	total := 0
	for i, x := range b {
		// 左の i 個に対しては +x、右の n-1-i 個に対しては -x
		total += x*i - x*(len(b)-1-i)
	}
	return total
}

// expectedRecords は 1..n のランダムな順列で最大値を更新する位置の個数の期待値を返す。
func expectedRecords(n int) float64 {
	e := 0.0
	for i := 1; i <= n; i++ {
		e += 1 / float64(i) // 位置 i が更新になる確率は 1/i
	}
	return e
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	fmt.Fprintln(out, sumOfAllSubarraySums(a))
	fmt.Fprintln(out, sumOfPairDiffs(a))
	fmt.Fprintf(out, "%.6f\n", expectedRecords(n))
}
