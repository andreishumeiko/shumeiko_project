m_dic = {}
with open("t_6.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        name, stats = line.split(':')
        name_s = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        m_dic[name] = name_s
print(f"{m_dic}")
