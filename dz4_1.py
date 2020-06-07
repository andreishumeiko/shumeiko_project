from sys import argv

script_name, hours_work, rate_hour = argv

def salary():
    if hours_work > 40:
        bonus = 200
    else:
        bonus = 0
    salary = float(hours_work) * float(rate_hour) + bonus
    return salary

print(script_name)
print("Your salary is: ", salary())
