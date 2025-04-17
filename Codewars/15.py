def perimeter(n):
    if n == 0:
        return 4
    
    fib = [1, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    total_perimeter = 0
    for side in fib:
        total_perimeter += 4 * side
    return total_perimeter

print(perimeter(5))
print(perimeter(7))