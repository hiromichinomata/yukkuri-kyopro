package main

import "fmt"

type line struct{ m, b int }

func main() {
	lines := []line{{1, 0}, {2, -1}, {3, -5}}
	dq := []line{}
	for _, ln := range lines {
		for len(dq) >= 2 {
			l1, l2, l3 := dq[len(dq)-2], dq[len(dq)-1], ln
			if (l2.b-l1.b)*(l3.m-l2.m) >= (l2.m-l1.m)*(l3.b-l2.b) {
				dq = dq[:len(dq)-1]
			} else {
				break
			}
		}
		dq = append(dq, ln)
	}
	eval := func(l line, x int) int { return l.m*x + l.b }
	fmt.Println(eval(dq[0], 0), eval(dq[0], 1), eval(dq[0], 2))
}
