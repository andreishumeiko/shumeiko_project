from collections import Counter


s_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(s_list)

counter = Counter(s_list)
new_list = [i for i,j in counter.items() if j == 1]
print(new_list)