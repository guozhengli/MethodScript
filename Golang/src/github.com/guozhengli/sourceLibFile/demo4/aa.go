package main

// 说明:
// 源码文件声明的包名可以与其所在目录的名称不同，只要这些 文件声明的包名一致就可以。

import "flag"

var name string

func init() {
	flag.StringVar(&name, "name", "everyone", "The greeting object.")
}

func main() {
	flag.Parse()
	hello(name)
}

// 执行命令
// go run main.go demo4_lib.go or 当前目录下 go build
