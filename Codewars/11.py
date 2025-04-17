def alphabet_position(text):
    word = "abcdefghijklmnopqrstuvwxyz"
    output = [] 

    for i in text.lower():
        if i in word:
            output.append(str(word.index(i) + 1))
    return " ".join(output)

print(alphabet_position("Hi my name is"))
