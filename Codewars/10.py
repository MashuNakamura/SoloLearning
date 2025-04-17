def likes(names):
    total_name = len(names)
    if total_name == 0:
        return "no one likes this"
    elif total_name == 1:
        return f"{names[0]} likes this"
    elif total_name == 2:
        return f"{names[0]} and {names[1]} like this"
    elif total_name == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {total_name - 2} others like this"

print(likes(["Yakult", "Yunli", "Pukimak", "Robert", "Putangina"]))
