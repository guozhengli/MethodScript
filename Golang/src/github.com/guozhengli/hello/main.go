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

	fmt.Println(KB)
	fmt.Println(MB)
	fmt.Println(GB)
	fmt.Println(TB)
}
