def get_count(sentence):
    tmp_total = 0
    vokal = ['a', 'i', 'u', 'e', 'o']
    for i in sentence:
        if i in vokal:
            tmp_total += 1
    return tmp_total

print(get_count("aiuhj"))
