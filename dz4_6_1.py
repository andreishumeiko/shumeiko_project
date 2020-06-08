from sys import argv
from itertools import count

script_name, start_point, end_point = argv

print(script_name)

for i in count(int(start_point)):
    if i > int(end_point):
        break
    else:
        print(i)

# Why can't I use generator? What is wrong? The line 7 only appear after I
# run the program. There is not any Errors.
#
# s_list = [i for i in count(int(start_point)) if i < int(end_point)]
# print(s_list)