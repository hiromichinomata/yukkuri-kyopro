package main

import "fmt"

func ccw(a, b, c [2]int) int {
	return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
}

func main() {
	fmt.Println(ccw([2]int{0, 0}, [2]int{1, 0}, [2]int{0, 1}))
}
