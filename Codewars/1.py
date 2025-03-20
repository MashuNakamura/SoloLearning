def hero(bullets, dragons):
    if dragons <= bullets / 2:
        return True
    else:
        return False

print(hero(4, 2))
