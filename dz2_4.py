s_string = input('Enter a string consisting of several words separated by spaces: ').split()

for i, word in enumerate(s_string, 1):
    print(f'{i} {word[:10]}')