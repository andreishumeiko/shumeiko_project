count = 0
with open("text.txt", "r", encoding='utf=8') as f:
    for line in f:
        count += 1
        line_w = line.split()
        print(line, 'The number of words: ', len(line_w))
    print('Tne number of lines: ', count)
