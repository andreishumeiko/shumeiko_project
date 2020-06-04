s_list = [1, 2.1, (-1 + 2j), True, 'Airplane', [5, 8], (5, 6.5), range(12), {1: 'fname', 2: 'lname'},
         (b'literal'), bytearray(b'twelve'), {8, 9}, frozenset(), zip(*[(5, 6), (18, 19), ('a', 'b')]), ValueError]

for i, item in enumerate(s_list):
    print(f"{i}. {item} - {type(item)}")