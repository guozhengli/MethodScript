package main

import (
	"container/ring"
	"fmt"
)

func main() {
	r := ring.New(5)

	n := r.Len()

	for i := 0; i < n; i++ {
		r.Value = i
		r = r.Next()
	}

	r.Do(func(p interface{}) {
		fmt.Println(p.(int))
	})
}
