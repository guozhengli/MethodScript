package main

import "fmt"

type AnimalCategory struct {
	kingdom string // 界。
	phylum  string // 门。
	class   string // 纲。
	order   string // 目。
	family  string // 科。
	genus   string // 属。
	species string // 种。
}

func (ac AnimalCategory) String() string {
	return fmt.Sprintf("kingdom: %s%s%s%s%s%s species:%s",
		ac.kingdom, ac.phylum, ac.class, ac.order,
		ac.family, ac.genus, ac.species)
}

func main() {
	d := AnimalCategory{kingdom: "dog"}
	c := AnimalCategory{species: "cat"}
	fmt.Printf("The animal category: %s %s \n", c, d)
}
