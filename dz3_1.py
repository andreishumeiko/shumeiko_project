def fdev(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'You cannot devide a by b=0'

try:
    print(fdev((float(input('Enter the first number: '))), (float(input('Enter the second number: ')))))
except ValueError:
    print('You have to use only numbers')
