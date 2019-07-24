package main

import "fmt"

const (
	a1 = iota
	a2 = 100
	a3
	a4 = iota
)

// 该常量为计量单位 折算数据大小使用
const (
	_  = iota
	KB = 1 << (10 * iota)
	MB = 1 << (10 * iota)
	GB = 1 << (10 * iota)
	TB = 1 << (10 * iota)
)

func main() {
	//fmt.Printf("Hello World~")
	//fmt.Println("a1: ", a1)
	//fmt.Println("a2: ", a2)
	//fmt.Println("a3: ", a3)
	//fmt.Println("a4: ", a4)

	// fmt.Println(KB)
	// fmt.Println(MB)
	// fmt.Println(GB)
	// fmt.Println(TB)

	// var a = make([]string, 5, 10)
	// for i := 0; i < 10; i++ {
	// 	a = append(a, fmt.Sprintf("%v", i))
	// }
	// fmt.Println(a)

	var badMap1 = map[int]string{}
	fmt.Printf("%v", badMap1)

	var map2 = map[interface{}]int{
		"aa": 1,
		"bb": 2,
		3:    3,
	}
	fmt.Printf("%v", map2)

}
