def capitalize(word):
    fl_small = word[0]
    fl_big = chr(ord(fl_small) - ord('a') + ord('A'))
    return fl_big + word[1:]


source = input('Enter your string in lower case: ').split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))