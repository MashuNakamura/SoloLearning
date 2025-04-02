package main

import (
	"fmt"
	f "fmt"
	t "time"
)

// func main() {
// 	fmt.Println("Hello World")
// 	fmt.Println(t.Now())
// }

func main() {
	// Are we racing or coding?
	/*	fmt.Println("Ready")
		fmt.Println("Set") */
	f.Println("Gooooo!")
	f.Println(t.DateTime)

	var stationName string
	var nextTrainTime int8
	var isUptownTrain bool

	stationName = "Union Square"
	nextTrainTime = 12
	isUptownTrain = false

	fmt.Println("Current station:", stationName)
	fmt.Println("Next train:", nextTrainTime, "minutes")
	fmt.Println("Is uptown:", isUptownTrain)

	stationName = "Grand Central"
	nextTrainTime = 3
	isUptownTrain = true

	fmt.Println("")
	fmt.Println("Current station:", stationName)
	fmt.Println("Next train:", nextTrainTime, "minutes")
	fmt.Println("Is uptown:", isUptownTrain)
}
