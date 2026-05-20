package main

import (
	"bufio"
	"fmt"
	"os"
)

func valid(s string) bool {
	st := []byte{}
	pair := map[byte]byte{')': '(', ']': '[', '}': '{'}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch == '(' || ch == '[' || ch == '{' {
			st = append(st, ch)
		} else if ch == ')' || ch == ']' || ch == '}' {
			if len(st) == 0 || st[len(st)-1] != pair[ch] {
				return false
			}
			st = st[:len(st)-1]
		}
	}
	return len(st) == 0
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var s string
	fmt.Fscan(in, &s)
	if valid(s) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
