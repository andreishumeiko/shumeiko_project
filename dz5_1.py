with open('text.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Input new string or empty string to end the program: ')
        if not line:
            break
        print(line, file=f)
