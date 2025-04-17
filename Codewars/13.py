def persistence(n):
    count = 0
    while n >= 10:
        total = 1
        for digit in str(n):
            total *= int(digit)
        n = total
        count += 1
    return count

print(persistence(39))
print(persistence(999))
print(persistence(4))
