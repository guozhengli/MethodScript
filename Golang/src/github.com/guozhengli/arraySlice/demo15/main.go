package main

import (
	"fmt"
)

func main() {
	s1 := make([]int, 5)
	fmt.Printf("%d\n", len(s1))             // 5
	fmt.Printf("%d\n", cap(s1))             // 5
	fmt.Printf("The value of s1: %d\n", s1) // [0,1,2,3,4] err [0,0,0,0,0]

	s2 := make([]int, 5, 8)
	fmt.Printf("%d\n", len(s2))
	fmt.Printf("%d\n", cap(s2)) // 8
	fmt.Printf("The value of s1: %d\n", s2)
	fmt.Println()

	s3 := []int{1, 2, 3, 4, 5, 6, 7, 8}
	s4 := s3[3:6]
	fmt.Printf("%d\n", len(s3))
	fmt.Printf("%d\n", cap(s3))
	fmt.Printf("%d\n", len(s4)) // 3
	fmt.Printf("%d\n", cap(s4)) // 3 猜错了，因为是从index 的3 开始截取的 往后不算 暂时这么理解 如果s3[2:3] 是从0，1，2(开始往后) 总长度8 - 2 = 6
	fmt.Printf("%d\n", s4)      // [4,5,6]
	fmt.Println()

	s5 := s4[:cap(s4)]
	fmt.Printf("The length of s5: %d\n", len(s5))   // 5
	fmt.Printf("The capacity of s5: %d\n", cap(s5)) // 5
	fmt.Printf("The value of s5: %d\n", s5)         // [4,5,6,7,8]
	fmt.Println()

	s6 := s3[:cap(s4)]
	fmt.Printf("The length of s5: %d\n", len(s6))   // 5
	fmt.Printf("The capacity of s5: %d\n", cap(s6)) // 8
	fmt.Printf("The value of s5: %d\n", s6)         // [1,2,3,4,5]

}
