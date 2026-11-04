package main

import "fmt"

type line struct{ m, b int }

func (l line) eval(x int) int { return l.m*x + l.b }

// chtMin は y = m*x + b の下包絡（最小値）を作る。
// 前提: lines は傾き m の降順、クエリ x は昇順。
func chtMin(lines []line) []line {
	dq := []line{}
	bad := func(l1, l2, l3 line) bool {
		// l1, l3 の交点が l1, l2 の交点より左（以下）なら l2 は最小にならない
		return (l3.b-l1.b)*(l1.m-l2.m) <= (l2.b-l1.b)*(l1.m-l3.m)
	}
	for _, ln := range lines {
		if len(dq) > 0 && dq[len(dq)-1].m == ln.m {
			if dq[len(dq)-1].b <= ln.b {
				continue
			}
			dq = dq[:len(dq)-1]
		}
		for len(dq) >= 2 && bad(dq[len(dq)-2], dq[len(dq)-1], ln) {
			dq = dq[:len(dq)-1]
		}
		dq = append(dq, ln)
	}
	return dq
}

// query は x が前回以上であることを前提に、先頭の直線を捨てながら最小値を返す。
func query(dq *[]line, x int) int {
	for len(*dq) >= 2 && (*dq)[0].eval(x) >= (*dq)[1].eval(x) {
		*dq = (*dq)[1:]
	}
	return (*dq)[0].eval(x)
}

func main() {
	lines := []line{{3, -5}, {2, -1}, {1, 0}} // 傾き降順
	dq := chtMin(lines)
	a := query(&dq, 0)
	b := query(&dq, 1)
	c := query(&dq, 2)
	fmt.Println(a, b, c)
}
