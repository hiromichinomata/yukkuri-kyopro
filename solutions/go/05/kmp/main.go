package main

import "fmt"

func buildNext(p string) []int {
	m := len(p)
	nxt := make([]int, m)
	j := 0
	for i := 1; i < m; i++ {
		for j > 0 && p[i] != p[j] {
			j = nxt[j-1]
		}
		if p[i] == p[j] {
			j++
			nxt[i] = j
		}
	}
	return nxt
}

func kmpSearch(text, pat string) []int {
	nxt := buildNext(pat)
	j := 0
	var pos []int
	for i := 0; i < len(text); i++ {
		for j > 0 && text[i] != pat[j] {
			j = nxt[j-1]
		}
		if text[i] == pat[j] {
			j++
		}
		if j == len(pat) {
			pos = append(pos, i-len(pat)+1)
			j = nxt[j-1]
		}
	}
	return pos
}

func main() {
	fmt.Println(kmpSearch("ababaabab", "aba"))
}
