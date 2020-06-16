r_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("t_41.txt", "a") as new_f:
    with open("t_4.txt") as m_f:
        line = m_f.read().split("\n")
        for i in line:
            i = i.split(" - ")
            new_f.writelines(r_dic[i[0]] + ' - ' + i[1] + "\n")

