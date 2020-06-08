from functools import reduce

s_list = [i for i in range(100, 1001) if i % 2 == 0]
print(s_list)

def multiply(prev_el, el):
    return prev_el * el

print(reduce(multiply,s_list))