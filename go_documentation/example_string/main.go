package example_string

import (
	"strings"
)

func Hello(text []string) string {
	// Menggabungkan elemen-elemen slice menjadi satu string
	message := "Hello, " + strings.Join(text, ", ")
	return message
}
