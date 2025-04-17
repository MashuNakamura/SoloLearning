def sum_mix(arr):
    total = 0
    for i in arr:
        if i == str(i):
            i = int(i)
        total += i
    return total

print(sum_mix([1, '2', 3, -4]))
