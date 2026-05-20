package main

import "fmt"

func analyzeConstraints(n, q, vmax int, graph bool) []string {
	var hints []string
	if n <= 20 {
		hints = append(hints, "bitmask / meet-in-the-middle")
	}
	if n <= 2000 && q <= 2000 {
		hints = append(hints, "O(N^2) DP or Floyd")
	}
	if graph {
		hints = append(hints, "tree? -> LCA/HLD; general -> flow/SCC/2-SAT")
	}
	if q >= 100000 {
		hints = append(hints, "log or sqrt decomposition, segtree/Fenwick")
	}
	if vmax <= 1000000 {
		hints = append(hints, "coordinate compression")
	}
	return hints
}

func main() {
	fmt.Println(analyzeConstraints(18, 0, 1_000_000_000, false))
	fmt.Println(analyzeConstraints(200000, 200000, 1_000_000_000, true))
}
