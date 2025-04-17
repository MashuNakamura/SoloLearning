def spin_words(sentence):
    word = ""
    this = sentence.split()

    for i in this:
        if len(i) >= 5:  
            word += i[::-1] + " "
        else:
            word += i + " "
    
    return word.strip()

print(spin_words("This Testing"))
print(spin_words("Hey fellow warriors"))
print(spin_words("Welcome to the challenge"))
