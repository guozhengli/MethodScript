package main

import "fmt"

func main() {
	s6 := make([]int, 0)
	fmt.Printf("The capacity of s6: %d\n", cap(s6))
	for i := 1; i <= 5; i++ {
		s6 = append(s6, i)
		// s6(1): len: 1, cap:1
		// s6(2): len: 2, cap:2
		// s6(3): len: 3, cap:4
		// s6(4): len: 4, cap:4
		// s6(5): len: 5, cap:8
		// 以上为输出结果 cap的变化是因为 如果新值超出原来的切片的容量则会2倍增量的加容量，直到1024 超过1024时以1.25倍增长加容量
		// 即 1时，容量为1 2时 2个位置容量大于目前的1个容量 所以 1*2 =2 扩充 到3时 3个容量大于目前2个容量所以 2*2 =4 以此类推
		fmt.Printf("s6(%d): len: %d, cap:%d\n", i, len(s6), cap(s6))
	}
	fmt.Println()

	// 示例2。 以1.25倍增长

	// 输出结果：
	// The capacity of s7: 1024
	// s7e1: len: 1224, cap: 1280
	// s7e2: len: 1424, cap: 1696
	// s7e3: len: 1624, cap: 2048

	s7 := make([]int, 1024)
	fmt.Printf("The capacity of s7: %d\n", cap(s7))
	s7e1 := append(s7, make([]int, 200)...)
	fmt.Printf("s7e1: len: %d, cap: %d\n", len(s7e1), cap(s7e1))
	s7e2 := append(s7, make([]int, 400)...)
	fmt.Printf("s7e2: len: %d, cap: %d\n", len(s7e2), cap(s7e2))
	s7e3 := append(s7, make([]int, 600)...)
	fmt.Printf("s7e3: len: %d, cap: %d\n", len(s7e3), cap(s7e3))
	fmt.Println()

	// 示例3。
	s8 := make([]int, 10)
	fmt.Printf("The capacity of s8: %d\n", cap(s8)) //10
	s8a := append(s8, make([]int, 11)...)
	fmt.Printf("s8a: len: %d, cap: %d\n", len(s8a), cap(s8a)) //21
	s8b := append(s8a, make([]int, 23)...)
	fmt.Printf("s8b: len: %d, cap: %d\n", len(s8b), cap(s8b))
	s8c := append(s8b, make([]int, 45)...)
	fmt.Printf("s8c: len: %d, cap: %d\n", len(s8c), cap(s8c))

}
