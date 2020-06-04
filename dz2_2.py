s_list = list(input("Enter arbitrary consequence of numbers without spaces: "))

for i in range(1, len(s_list), 2):
    s_list[i - 1], s_list[i] = s_list[i], s_list[i - 1]

print(s_list)