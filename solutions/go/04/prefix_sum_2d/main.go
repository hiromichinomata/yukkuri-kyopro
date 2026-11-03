package main

import "fmt"

// build2D は s[i][j] = 左上 i 行 j 列の和（1 始まり）を作る
func build2D(a [][]int) [][]int {
	h, w := len(a), len(a[0])
	s := make([][]int, h+1)
	for i := range s {
		s[i] = make([]int, w+1)
	}
	for i := 1; i <= h; i++ {
		for j := 1; j <= w; j++ {
			s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i-1][j-1]
		}
	}
	return s
}

// rectSum は (h1, w1) から (h2, w2) まで（両端を含む、1 始まり）の矩形の和
func rectSum(s [][]int, h1, w1, h2, w2 int) int {
	return s[h2][w2] - s[h1-1][w2] - s[h2][w1-1] + s[h1-1][w1-1]
}

func main() {
	a := [][]int{{1, 2, 3}, {4, 5, 6}}
	s := build2D(a)
	fmt.Println(rectSum(s, 1, 1, 2, 2))
}
