package main

import (
	"errors"
	"fmt"
	"go_documentation/example_string"
	"math/rand"
)

func DetectError(name string) (string, error) {
	if name == "" {
		return name, errors.New("Empty Name")
	}
	message := fmt.Sprintf(randomFormat(), name)
	return message, nil
}

func randomFormat() string {
	formats := []string{
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hail, %v! Well met!",
	}
	return formats[rand.Intn(len(formats))]
}

// Multiple Random

func Hellos(names []string) (map[string]string, error) {
	messages := make(map[string]string)
	for _, name := range names {
		message, err := DetectError(name)
		if err != nil {
			continue
		}
		messages[name] = message
	}
	return messages, nil
}

func main() {
	names := []string{"Gladys", "Samantha", "Darrin", ""}
	message := example_string.Hello(names)
	fmt.Println(message)
}
