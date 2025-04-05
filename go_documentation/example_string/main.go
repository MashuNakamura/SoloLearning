package example_string

import "fmt"

func Hello(text string) string {
	message := fmt.Sprint("Hello, ", text)
	return message
}

func main() {
	result := Hello("Matthew")
	fmt.Println(result)
}
