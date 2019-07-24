package main

import (
	"fmt"
	"unsafe"
)

func main() {
	complexArray1 := [3][]string{
		[]string{"d", "e", "f"},
		[]string{"g", "h", "i"},
		[]string{"j", "k", "l"},
	}

	// array1 := [3]string{"a", "b", "c"}
	fmt.Printf("The array:%v\n", complexArray1)
	array2 := modifyComplexArray(complexArray1)
	fmt.Printf("The modified array: %v %v \n", array2, unsafe.Pointer(&array2))
	fmt.Printf("The original array: %v %v\n", complexArray1, unsafe.Pointer(&complexArray1))

}

func modifyComplexArray(a [3][]string) [3][]string {
	a[1][1] = "1111"
	a[2] = []string{"o", "p", "q"}
	return a
}

// The modified array:["a", "x", "c"]
// The original array: ["a", "x", "c"]
