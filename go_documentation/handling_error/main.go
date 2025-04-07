package main

import (
	"errors"
	"fmt"
	"log"
)

// Example of Handing Error

func detect_error(name string) (string, error) {
	if name == "" {
		return "", errors.New("Empty Name")
	}
	message := fmt.Sprintf("Hi, %v.", name)
	return message, nil
}

func main() {
	name := "Matthew"
	display_name, err := detect_error(name)
	if err != nil {
		fmt.Println("Error", err)
		log.Fatal(err)
	} else {
		fmt.Println(display_name)
	}
}
