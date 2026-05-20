package main

import "fmt"

const mod = 1_000_000_007

func gauss(A [][]int) [][]int {
	n := len(A)
	m := len(A[0])
	row := 0
	for col := 0; col < m-1; col++ {
		pivot := -1
		for r := row; r < n; r++ {
			if A[r][col]%mod != 0 {
				pivot = r
				break
			}
		}
		if pivot == -1 {
			continue
		}
		A[row], A[pivot] = A[pivot], A[row]
		inv := powMod(A[row][col], mod-2)
		for c := col; c < m; c++ {
			A[row][c] = A[row][c] * inv % mod
		}
		for r := 0; r < n; r++ {
			if r == row {
				continue
			}
			factor := A[r][col]
			if factor == 0 {
				continue
			}
			for c := col; c < m; c++ {
				A[r][c] = (A[r][c] - factor*A[row][c]%mod + mod) % mod
			}
		}
		row++
	}
	return A
}

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

func main() {
	A := [][]int{{2, 1, 5}, {1, 1, 3}}
	fmt.Println(gauss(A))
}
