package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type interval struct{ start, end int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	ivs := make([]interval, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &ivs[i].start, &ivs[i].end)
	}
	sort.Slice(ivs, func(i, j int) bool {
		return ivs[i].end < ivs[j].end
	})
	last := -1 << 60
	cnt := 0
	for _, iv := range ivs {
		if iv.start >= last {
			cnt++
			last = iv.end
		}
	}
	fmt.Println(cnt)
}
