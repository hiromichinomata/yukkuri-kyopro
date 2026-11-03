package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// compress は値の一覧を、小さい順に 1, 2, … の番号へ置き換える表を作る
func compress(vs []int) map[int]int {
	u := append([]int(nil), vs...)
	sort.Ints(u)
	id := map[int]int{}
	for _, v := range u {
		if _, ok := id[v]; !ok {
			id[v] = len(id) + 1
		}
	}
	return id
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var h, w, n int
	fmt.Fscan(in, &h, &w, &n)
	a, b := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &a[i], &b[i])
	}
	// 数字のある行・列だけが残る → 行番号・列番号をそれぞれ座標圧縮すればよい
	ra, rb := compress(a), compress(b)
	for i := 0; i < n; i++ {
		fmt.Fprintln(out, ra[a[i]], rb[b[i]])
	}
}
