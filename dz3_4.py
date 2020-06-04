def my_func(x, y):
    while x > 0:
        while y <= 0:
            for i in range(abs(y + 1)):
                x *= x
                d = 1 / x
                return d
        else:
            print('You have to enter negative integer power')
            break
    else:
        print('You have to enter positive real base')

try:
    print(my_func((float(input('Enter the base: '))), (int(input('Enter the base: ')))))
except ValueError:
    print('You have to enter negative integer power')
