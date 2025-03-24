def accum(st):
    total = []
    for i, char in enumerate(st):
        formatted = char.upper() + char.lower() * i
        total.append(formatted)
    return "-".join(total)

print(accum("abc"))
