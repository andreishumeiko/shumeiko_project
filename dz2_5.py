s_list = [8, 7, 5, 5, 2]

new_num = int(input("Enter a new rating number: "))
i = 0
for n in s_list:
    if new_num <= n:
        i += 1
s_list.insert(i, float(new_num))
print(s_list)

