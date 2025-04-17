# Fizz Buzz

number_counter = 1 

while number_counter <= 100:
    if number_counter % 3 == 0 and number_counter % 5 == 0:
        print("FizzBuzz")
    elif number_counter % 3 == 0:
        print("Fizz")
    elif number_counter % 5 == 0:
        print("Buzz")
    else:
        print(number_counter)
    number_counter += 1
