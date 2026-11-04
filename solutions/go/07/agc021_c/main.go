package main

import (
	"bufio"
	"fmt"
	"os"
)

// fill は敷き詰めを試す。成功すれば盤面、失敗すれば nil
func fill(n, m, a, b int, pinwheel bool) [][]byte {
	g := make([][]byte, n)
	for i := range g {
		g[i] = make([]byte, m)
		for j := range g[i] {
			g[i][j] = '.'
		}
	}
	skipI, skipJ := -1, -1
	if pinwheel {
		// 右下 3×3 に「風車」型で 1×2 を 2 枚、2×1 を 2 枚置く（中央は空き）
		r, c := n-3, m-3
		pat := []string{"<>^", "^.v", "v<>"}
		for i := 0; i < 3; i++ {
			for j := 0; j < 3; j++ {
				g[r+i][c+j] = pat[i][j]
			}
		}
		a -= 2
		b -= 2
		skipI, skipJ = n-3, m-3 // 風車と重なる 2×2 ブロック
	}
	if n%2 == 1 { // 最後の行: 1×2 を左から
		for j := 0; j+1 < m; j += 2 {
			if a > 0 && g[n-1][j] == '.' && g[n-1][j+1] == '.' {
				g[n-1][j], g[n-1][j+1] = '<', '>'
				a--
			}
		}
	}
	if m%2 == 1 { // 最後の列: 2×1 を上から
		for i := 0; i+1 < n; i += 2 {
			if b > 0 && g[i][m-1] == '.' && g[i+1][m-1] == '.' {
				g[i][m-1], g[i+1][m-1] = '^', 'v'
				b--
			}
		}
	}
	for i := 0; i < n-n%2; i += 2 { // 残りの 2×2 ブロック
		for j := 0; j < m-m%2; j += 2 {
			if i == skipI && j == skipJ {
				continue
			}
			if a > 0 {
				g[i][j], g[i][j+1] = '<', '>'
				a--
				if a > 0 {
					g[i+1][j], g[i+1][j+1] = '<', '>'
					a--
				}
			} else if b > 0 {
				g[i][j], g[i+1][j] = '^', 'v'
				b--
				if b > 0 {
					g[i][j+1], g[i+1][j+1] = '^', 'v'
					b--
				}
			}
		}
	}
	if a != 0 || b != 0 {
		return nil
	}
	return g
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m, a, b int
	fmt.Fscan(in, &n, &m, &a, &b)
	tries := []bool{false}
	if n%2 == 1 && m%2 == 1 && n >= 3 && m >= 3 && a >= 2 && b >= 2 {
		tries = append(tries, true) // 両方奇数のときは、風車を使うと 1 マス分得をすることがある
	}
	for _, pw := range tries {
		if g := fill(n, m, a, b, pw); g != nil {
			fmt.Fprintln(out, "YES")
			for _, row := range g {
				fmt.Fprintln(out, string(row))
			}
			return
		}
	}
	fmt.Fprintln(out, "NO")
}
