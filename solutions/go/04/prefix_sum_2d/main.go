package main

import "fmt"

func main() {
	a := [][]int{{1, 2, 3}, {4, 5, 6}}
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
	rect := s[2][2] - s[0][2] - s[2][0] + s[0][0]
	fmt.Println(rect)
}
