package main

import (
	"flag"
	"fmt"
)

var name string

func main() {
	flag.StringVar(&name, "name", "somebody", "说明")
	flag.Parse()
	fmt.Printf("your send your name: %s", name)
}
