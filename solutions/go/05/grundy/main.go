package main

import "fmt"

func nimWinner(piles []int) string {
	x := 0
	for _, p := range piles {
		x ^= p
	}
	if x != 0 {
		return "first"
	}
	return "second"
}

func main() {
	fmt.Println(nimWinner([]int{1, 2, 3}))
	fmt.Println(nimWinner([]int{2, 2}))
}
