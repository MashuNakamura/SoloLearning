package example_string

import (
	"strings"
)

// This file gonna be main of the string message
func Hello(text []string) string {
	message := "Hello, " + strings.Join(text, ", ")
	return message
}
