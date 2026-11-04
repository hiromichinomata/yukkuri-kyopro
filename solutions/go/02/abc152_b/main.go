package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var a, b int
	fmt.Fscan(in, &a, &b)
	s := strings.Repeat(strconv.Itoa(a), b) // 数字 a を b 個
	t := strings.Repeat(strconv.Itoa(b), a) // 数字 b を a 個
	if s < t {                              // string の < は辞書順
		fmt.Fprintln(out, s)
	} else {
		fmt.Fprintln(out, t)
	}
}
