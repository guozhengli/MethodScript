package main

import (
	"errors"
	"fmt"
)

type operate func(x, y int) int

type calculateFunc func(x int, y int) (int, error)

func getCalculator(op operate) calculateFunc {
	return func(x int, y int) (int, error) {
		if op == nil {
			return 0, errors.New("invalid operation")
		}
		return op(x, y), nil
	}
}

func main() {
	x, y := 10, 5000
	op := func(x, y int) int {
		return x + y
	}

	add := getCalculator(op)
	result, err := add(x, y)
	fmt.Printf("The result: %d (error: %v)\n", result, err)
}
