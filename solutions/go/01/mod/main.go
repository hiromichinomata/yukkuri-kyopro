package main

import "fmt"

const mod = 998244353

func addMod(a, b, m int) int {
	return (a + b) % m
}

func main() {
	fmt.Println(addMod(1_000_000_000, 1_000_000_000, mod))
}
