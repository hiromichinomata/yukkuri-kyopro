package main

import "fmt"

func scc(g [][]int, n int) []int {
	order := []int{}
	seen := make([]bool, n)
	var dfs func(v int)
	dfs = func(v int) {
		seen[v] = true
		for _, to := range g[v] {
			if !seen[to] {
				dfs(to)
			}
		}
		order = append(order, v)
	}
	for i := 0; i < n; i++ {
		if !seen[i] {
			dfs(i)
		}
	}
	rg := make([][]int, n)
	for v := 0; v < n; v++ {
		for _, to := range g[v] {
			rg[to] = append(rg[to], v)
		}
	}
	comp := make([]int, n)
	cid := 0
	seen = make([]bool, n)
	var rdfs func(v int)
	rdfs = func(v int) {
		seen[v] = true
		comp[v] = cid
		for _, to := range rg[v] {
			if !seen[to] {
				rdfs(to)
			}
		}
	}
	for i := n - 1; i >= 0; i-- {
		v := order[i]
		if !seen[v] {
			rdfs(v)
			cid++
		}
	}
	return comp
}

// リテラルの番号: 2*i が「x_i が真」、2*i+1 が「x_i が偽」。l ^ 1 で否定になる
// addClause: 節 (a ∨ b) は「¬a なら b」「¬b なら a」の 2 本の含意
func addClause(implications [][2]int, a, b int) [][2]int {
	return append(implications, [2]int{a ^ 1, b}, [2]int{b ^ 1, a})
}

func sat2Solvable(implications [][2]int, nVars int) bool {
	n := 2 * nVars
	g := make([][]int, n)
	for _, e := range implications {
		g[e[0]] = append(g[e[0]], e[1])
	}
	comp := scc(g, n)
	for i := 0; i < nVars; i++ {
		if comp[2*i] == comp[2*i+1] {
			return false
		}
	}
	return true
}

func yesNo(b bool) string {
	if b {
		return "Yes"
	}
	return "No"
}

func main() {
	// (x0 ∨ x1) ∧ (¬x0 ∨ x1) ∧ (¬x1 ∨ x0) → x0 = x1 = 真 で充足可能
	var imp [][2]int
	imp = addClause(imp, 0, 2)
	imp = addClause(imp, 1, 2)
	imp = addClause(imp, 3, 0)
	fmt.Println(yesNo(sat2Solvable(imp, 2)))
	// さらに (¬x0 ∨ ¬x1) を足すと充足不能
	imp = addClause(imp, 1, 3)
	fmt.Println(yesNo(sat2Solvable(imp, 2)))
}
