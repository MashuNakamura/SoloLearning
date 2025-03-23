def array_diff(a, b):
    tmp = []
    for i in a:
        if i not in b:
            tmp.append(i)
    return tmp

a = [1, 2, 3, 4]
b = [1, 3]
tmp = array_diff(a, b)
print(tmp)
