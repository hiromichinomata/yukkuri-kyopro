package main

import (
	"fmt"
	"sort"
)

func suffixArray(s string) []int {
	n := len(s)
	sa := make([]int, n)
	for i := range sa {
		sa[i] = i
	}
	rank := make([]int, n)
	for i, c := range s {
		rank[i] = int(c)
	}
	for k := 1; k < n; k <<= 1 {
		sort.Slice(sa, func(i, j int) bool {
			ri, rj := rank[sa[i]], rank[sa[j]]
			if ri != rj {
				return ri < rj
			}
			ai, aj := -1, -1
			if sa[i]+k < n {
				ai = rank[sa[i]+k]
			}
			if sa[j]+k < n {
				aj = rank[sa[j]+k]
			}
			return ai < aj
		})
		newRank := make([]int, n)
		newRank[sa[0]] = 0
		for i := 1; i < n; i++ {
			prev, cur := sa[i-1], sa[i]
			a1, a2 := rank[prev], rank[cur]
			b1, b2 := -1, -1
			if prev+k < n {
				b1 = rank[prev+k]
			}
			if cur+k < n {
				b2 = rank[cur+k]
			}
			less := a1 < a2 || (a1 == a2 && b1 < b2)
			newRank[cur] = newRank[prev]
			if less {
				newRank[cur]++
			}
		}
		rank = newRank
		if rank[sa[n-1]] == n-1 {
			break
		}
	}
	return sa
}

func main() {
	s := "banana"
	sa := suffixArray(s)
	fmt.Println(sa)
}
