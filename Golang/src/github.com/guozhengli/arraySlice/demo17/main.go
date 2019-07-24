package main

import "fmt"

func main() {
	// 输出结果
	// API server listening at: 127.0.0.1:42626
	// a1: [1 2 3 4 5 6 7] (len: 7, cap: 7)
	// s9: [2 3 4] (len: 3, cap: 6)
	// s9(1): [2 3 4 1] (len: 4, cap: 6)
	// s9(2): [2 3 4 1 2] (len: 5, cap: 6)
	// s9(3): [2 3 4 1 2 3] (len: 6, cap: 6)
	// s9(4): [2 3 4 1 2 3 4] (len: 7, cap: 12)
	// s9(5): [2 3 4 1 2 3 4 5] (len: 8, cap: 12)
	// a1: [1 2 3 4 1 2 3] (len: 7, cap: 7)

	// 示例1。
	a1 := [7]int{1, 2, 3, 4, 5, 6, 7}
	// a1:[1, 2, 3, 4, 5, 6, 7](len: 7, cap:7)
	fmt.Printf("a1: %v (len: %d, cap: %d)\n",
		a1, len(a1), cap(a1))
	// a1: 2,3,4 len:3 cap:6
	s9 := a1[1:4]
	//s9[0] = 1
	fmt.Printf("s9: %v (len: %d, cap: %d)\n",
		s9, len(s9), cap(s9))
	for i := 1; i <= 5; i++ {
		s9 = append(s9, i)
		// 1, [2,3,4,1] len4 cap 6
		// ... 2 : 5 6 3: 6 6 4:7 12 5:8 12
		fmt.Printf("s9(%d): %v (len: %d, cap: %d)\n",
			i, s9, len(s9), cap(s9))
	}
	fmt.Printf("a1: %v (len: %d, cap: %d)\n",
		a1, len(a1), cap(a1))
	fmt.Println()

}
