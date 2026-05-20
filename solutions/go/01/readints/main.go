package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readInts(in *bufio.Reader, n int) []int {
	line, _ := in.ReadString('\n')
	fields := strings.Fields(strings.TrimSpace(line))
	xs := make([]int, n)
	for i := 0; i < n; i++ {
		xs[i], _ = strconv.Atoi(fields[i])
	}
	return xs
}

func main() {
	in := bufio.NewReader(os.Stdin)
	xs := readInts(in, 3)
	fmt.Println(xs)
}
