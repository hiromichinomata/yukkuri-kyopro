package main

import (
	"bufio"
	"fmt"
	"os"
)

// construct は 1..n を和の等しい 2 グループに分ける。不可能なら ok=false。
// 必要条件: 総和 n(n+1)/2 が偶数 ⇔ n%4 が 0 か 3。これは十分でもある。
func construct(n int) (a, b []int, ok bool) {
	if n%4 == 1 || n%4 == 2 {
		return nil, nil, false
	}
	start := 1
	if n%4 == 3 {
		a = append(a, 1, 2) // 1 + 2 = 3 で釣り合わせてから、残り 4..n を 4 個ずつ処理
		b = append(b, 3)
		start = 4
	}
	// 連続する 4 個 k, k+1, k+2, k+3 は k + (k+3) = (k+1) + (k+2) で分けられる
	for k := start; k <= n; k += 4 {
		a = append(a, k, k+3)
		b = append(b, k+1, k+2)
	}
	return a, b, true
}

func printInts(out *bufio.Writer, xs []int) {
	for i, x := range xs {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, x)
	}
	fmt.Fprintln(out)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	a, b, ok := construct(n)
	if !ok {
		fmt.Fprintln(out, -1)
		return
	}
	// 小さい順に並べて出力（a, b はどちらも昇順に積んでいる）
	printInts(out, a)
	printInts(out, b)
}
