# While 

guess = 0
life = 3

while guess != 6:
    print(f"Current Chance : ", life)
    guess = int(input("Guess the number: "))
    life -= 1
    if life > 0:
        continue
    else:
        print("You Lose")
        break
else:
    print("You got it!")
