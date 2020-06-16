with open("t_salary.txt", "r", encoding="utf-8") as f:
    p_sum = []
    less = []
    line = f.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        p_sum.append(i[1])

print(f"Salary less 20000 {less}. Average salary: {sum(map(float, p_sum)) / len(p_sum)}")
