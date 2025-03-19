n = 4
bil = 1

for y in range (0, n):
    for _ in range (y, n):
        print(" ", end=" ")
    for _ in range (0, y + 1):
        print(bil, end=" ")
        bil+=1
    print()

# Note : It only spam print() but i use loop instead, hehe
