def fsum(a, b, c):
    d = [a, b, c]
    d.remove(min(a, b, c))
    return sum(d)


try:
    print(fsum((float(input('Enter the first number: '))), (float(input('Enter the second number: '))),
               (float(input('Enter the first number: ')))))
except ValueError:
    print('You have to use only numbers')