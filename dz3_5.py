def fstr():
    res = 0
    while True:
        numbers = input('Enter list of numbers or # to exit: ').split()
        for i in numbers:
            try:
                if i == '#':
                    print(f'Sum is {res}. You left the program')
                    return
                else:
                    res += float(i)
            except ValueError:
                print('Enter numbers or #')
        print(f'Sum is {res}')

print(fstr())