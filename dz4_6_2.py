from sys import argv
from itertools import cycle

# In case a list is already set
# script_name, s_condition = argv
#
# print(script_name)
#
# s_list = [5, 6, 7, 8]
#
# c = 0
# for i in cycle(s_list):
#     if c > int(s_condition):
#         break
#     print(i)
#     c += 1

# In case a list is required to set in parameters

script_name, s_list, s_condition = argv

print(script_name)

c = 0
for i in cycle(s_list):
    if c > int(s_condition):
        break
    print(i)
    c += 1