package main

/*
flag 练习
flag  命令源码文件接收参数并打印接受的内容

命令行输出内容：
➜  hello_somebody git:(Goland) ✗ go run main.go
Hello, 任何人!
➜  hello_somebody git:(Goland) ✗ go run main.go --help
Usage of /var/folders/b2/tj_h9hcj78l8j9x61l1d9ps80000gn/T/go-build940172882/b001/exe/main:
  -name string
        测试下支持中文吗？ (default "任何人")
exit status 2
➜  hello_somebody git:(Goland) ✗ go run main.go -name="ligz"
Hello, ligz!
➜  hello_somebody git:(Goland) ✗

Usage of /var/folders/b2/tj_h9hcj78l8j9x61l1d9ps80000gn/T/go-build940172882/b001/exe/main:
是go run命令构建上述命令源码文件时临时生成的可执行文件的完整路径

➜  hello_somebody git:(Goland) ✗ go build
➜  hello_somebody git:(Goland) ✗ ls
hello_somebody main.go
➜  hello_somebody git:(Goland) ✗ ./hello_somebody --help
Usage of ./hello_somebody:
  -name string
        测试下支持中文吗？ (default "任何人")

*/

import (
	// 需要在此处添加代码. [1]
	"flag"
	"fmt"
	"os"
)

// 创建一个私有的命令 参数容器
var cmdline = flag.NewFlagSet("question", flag.ExitOnError) // self define

var nameVar string

func init() {
	// 我们在调用flag包中的一些函数(比如StringVar、Parse等等)的时 候，
	//	   实际上是在调用flag.CommandLine变量的对应方法
	// 这个命令使用时失败了 后续查询下原因。。 错误原因是因为这段需要放到init函数中 我之前写到了main中了！

	flag.CommandLine = flag.NewFlagSet(os.Args[0], flag.ExitOnError)
	flag.CommandLine.Usage = func() {
		fmt.Fprintf(os.Stderr, "帮助信息\n")
		flag.PrintDefaults()
	}

	// [2]
	// flag.StringVar(&nameVar, "name", "任何人", "测试下支持中文吗？")
	cmdline.StringVar(&nameVar, "name", "任何人", "测试下支持中文吗？") // self define

}

// 同一区域存在多个main函数 此处注释掉 查看测试结果时取消main函数注释即可！

func main() {
	// [3]
	// 编写help展示信息
	// flag.Usage = func() {
	// 	fmt.Fprintf(os.Stderr, "帮助信息\n")
	// 	flag.PrintDefaults()
	// }

	// flag使用文档：https://golang.google.cn/pkg/flag/

	// 启动本地go docs 文档
	// 说明使用地址：https://github.com/hyper0x/go_command_tutorial/blob/master/0.5.md

	// flag.Parse()
	cmdline.Parse(os.Args[1:]) // self define
	fmt.Printf("Hello, %s!\n", nameVar)

}
