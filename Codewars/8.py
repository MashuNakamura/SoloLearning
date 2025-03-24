def solution(number):
    total = 0
    if number > 0:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                total += i
    else:
        total = 0
    return total

print(solution(50))
