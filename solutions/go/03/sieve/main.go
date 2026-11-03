package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// sieve は isP[i] が true なら i が素数（0 <= i <= n）となる表を返す。
func sieve(n int) []bool {
	isP := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		isP[i] = true
	}
	for i := 2; i*i <= n; i++ {
		if isP[i] {
			for j := i * i; j <= n; j += i { // i*i 未満は小さい素数で消し済み
				isP[j] = false
			}
		}
	}
	return isP
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	isP := sieve(n)
	primes := []string{}
	for i := 0; i <= n; i++ {
		if isP[i] {
			primes = append(primes, fmt.Sprint(i))
		}
	}
	fmt.Fprintln(out, len(primes))
	fmt.Fprintln(out, strings.Join(primes, " "))
}
