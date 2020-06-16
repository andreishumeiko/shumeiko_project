from random import randint

sum_el = 0
with open("t.txt", "w", encoding="utf-8") as m_f:
    for i in range(1000):
        el = randint(1, 1000)
        sum_el += el
        m_f.write(str(el) + " ")

print(f"Sum of elements: {sum_el}")