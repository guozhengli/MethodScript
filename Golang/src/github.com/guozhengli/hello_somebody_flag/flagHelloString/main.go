package main

import (
	"flag"
	"fmt"
)

var name = flag.String("name", "everyone", "the mettings")

// 同一区域存在多个main函数 此处注释掉 查看测试结果时取消main函数注释即可！

func main() {
	flag.Parse()
	fmt.Printf("Hello, %s!\n", *name)
}
