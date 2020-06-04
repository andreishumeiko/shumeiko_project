try:
    month = int(input("Enter the number corresponding to the month you are interested in: "))

    if 0 <= int(month) <= 12:
        s_1 = ['winter', 'spring', 'summer', 'autumn']
        s_2 = {0: 'winer', 1: 'spring', 2: 'summer', 3: 'autumn', 4: 'winter'}
        print(f'This month refers to {s_1[int(month) // 3]} season')
    else:
        print("Probably you don't know how much months are in a year")
except ValueError:
    print("Probably you don't know how much months are in a year")
