package main

import "fmt"

type ahoCorasick struct {
	next  []map[rune]int
	fail  []int
	out   [][]int // そのノードで終わるパターン番号（失敗リンク先の分も含む）
	words []string
}

func newAhoCorasick() *ahoCorasick {
	return &ahoCorasick{next: []map[rune]int{{}}, fail: []int{0}, out: [][]int{nil}}
}

func (ac *ahoCorasick) add(s string) {
	node := 0
	for _, ch := range s {
		nxt, ok := ac.next[node][ch]
		if !ok {
			nxt = len(ac.next)
			ac.next[node][ch] = nxt
			ac.next = append(ac.next, map[rune]int{})
			ac.fail = append(ac.fail, 0)
			ac.out = append(ac.out, nil)
		}
		node = nxt
	}
	ac.out[node] = append(ac.out[node], len(ac.words))
	ac.words = append(ac.words, s)
}

func (ac *ahoCorasick) build() {
	q := []int{}
	for _, nxt := range ac.next[0] {
		q = append(q, nxt)
	}
	for len(q) > 0 {
		v := q[0]
		q = q[1:]
		for ch, nxt := range ac.next[v] {
			f := ac.fail[v]
			for f != 0 {
				if _, ok := ac.next[f][ch]; ok {
					break
				}
				f = ac.fail[f]
			}
			ac.fail[nxt] = ac.next[f][ch] // 無ければ 0（根）
			// 失敗リンク先で終わるパターンも、ここで終わっている
			ac.out[nxt] = append(append([]int{}, ac.out[nxt]...), ac.out[ac.fail[nxt]]...)
			q = append(q, nxt)
		}
	}
}

type hit struct {
	end  int
	word string
}

// search は (終了位置, パターン) の一覧を返す。
func (ac *ahoCorasick) search(text string) []hit {
	node := 0
	hits := []hit{}
	for i, ch := range []rune(text) {
		for node != 0 {
			if _, ok := ac.next[node][ch]; ok {
				break
			}
			node = ac.fail[node]
		}
		node = ac.next[node][ch]
		for _, k := range ac.out[node] {
			hits = append(hits, hit{i, ac.words[k]})
		}
	}
	return hits
}

func main() {
	ac := newAhoCorasick()
	for _, w := range []string{"he", "she", "his", "hers"} {
		ac.add(w)
	}
	ac.build()
	for _, h := range ac.search("ushers") {
		fmt.Println(h.end, h.word)
	}
}
