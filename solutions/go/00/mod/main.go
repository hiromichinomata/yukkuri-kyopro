package main

import "fmt"

const mod = 998244353

func addMod(a, b, m int) int {
	return (a + b) % m
}

func mulMod(a, b, m int) int {
	return a * b % m // a, b < m なら a*b は int64 に収まる
}

func main() {
	fmt.Println(addMod(1_000_000_000, 1_000_000_000, mod))
	fmt.Println(mulMod(100_000, 100_000, mod))
}
