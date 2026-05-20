package main

import "fmt"

func countCoprime(n int) int {
	primes := []int{2, 3}
	ans := n
	m := len(primes)
	for mask := 1; mask < 1<<m; mask++ {
		bits := 0
		prod := 1
		for i := 0; i < m; i++ {
			if mask>>i&1 == 1 {
				bits++
				prod *= primes[i]
			}
		}
		if bits%2 == 1 {
			ans -= n / prod
		} else {
			ans += n / prod
		}
	}
	return ans
}

func main() {
	fmt.Println(countCoprime(30))
}
