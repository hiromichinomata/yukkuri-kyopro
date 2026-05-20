package main

import "fmt"

const mod = 1_000_000_007

func matMul(A, B [][]int) [][]int {
	n, m, p := len(A), len(B), len(B[0])
	C := make([][]int, n)
	for i := range C {
		C[i] = make([]int, p)
	}
	for i := 0; i < n; i++ {
		for k := 0; k < m; k++ {
			if A[i][k] == 0 {
				continue
			}
			for j := 0; j < p; j++ {
				C[i][j] = (C[i][j] + A[i][k]*B[k][j]) % mod
			}
		}
	}
	return C
}

func matPow(M [][]int, e int) [][]int {
	n := len(M)
	res := make([][]int, n)
	for i := 0; i < n; i++ {
		res[i] = make([]int, n)
		res[i][i] = 1
	}
	for e > 0 {
		if e&1 == 1 {
			res = matMul(res, M)
		}
		M = matMul(M, M)
		e >>= 1
	}
	return res
}

func fib(n int) int {
	if n == 0 {
		return 0
	}
	T := [][]int{{1, 1}, {1, 0}}
	Tn := matPow(T, n-1)
	return Tn[0][0]
}

func main() {
	for n := 0; n < 10; n++ {
		fmt.Print(fib(n), " ")
	}
	fmt.Println()
}
