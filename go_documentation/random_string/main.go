package main

import (
	"errors"
	"fmt"
	"log"
	"math/rand"
)

// Random String

func randomFormat() string {
	formats := []string{
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hail, %v! Well met!",
	}

	return formats[rand.Intn(len(formats))]
}

func detect_error(name string) (string, error) {
	if name == "" {
		return "", errors.New("Empty Name")
	}
	message := fmt.Sprintf(randomFormat(), name)
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
