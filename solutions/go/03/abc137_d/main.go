package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	jobs := make([][2]int, n)
	maxd := 0
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &jobs[i][0], &jobs[i][1])
		if jobs[i][0] > maxd {
			maxd = jobs[i][0]
		}
	}
	sort.Slice(jobs, func(i, j int) bool {
		return jobs[i][0] < jobs[j][0]
	})
	dp := make([]int, maxd+2)
	for _, job := range jobs {
		d, p := job[0], job[1]
		for i := maxd; i >= d; i-- {
			if dp[d-1]+p > dp[i] {
				dp[i] = dp[d-1] + p
			}
		}
	}
	ans := 0
	for _, v := range dp {
		if v > ans {
			ans = v
		}
	}
	fmt.Println(ans)
}
