def generate_hashtag(s: str):
    words = s.strip().split()
    if not words:
        return False
    capitalized = [word.capitalize() for word in words]
    result = '#' + ''.join(capitalized)
    if len(result) > 140:
        return False
    return result

s = "h   e ll o wor l d"
result = generate_hashtag(s)
print(result)