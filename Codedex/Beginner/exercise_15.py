# The Cyclone

tall = int(input("Input Height : "))
credit = int(input("Input Credit : "))

if tall >= 120 and credit >= 5000:
    print("Enjoy the vibes !")
elif tall <= 120 and credit >= 5000:
    print("Not enough Tall")
elif tall >= 120 and credit <= 5000:
    print("Not enough credit")
else:
    print("Can't have a ride")
