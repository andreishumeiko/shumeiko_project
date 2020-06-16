import json

result = []
with open("m_t7.json", "w", encoding="utf-8") as write_f:
    with open("t_7.txt", encoding="utf-8") as f_obj:
        profit = {}
        for line in f_obj:
            profit[line.split(' ')[0]] = float(line.split(' ')[2]) - float(line.split(' ')[3])
            average_profit = sum([float(i) for i in profit.values() if float(i) > 0]) / len(
                [float(i) for i in profit.values() if float(i) > 0])
        result.append(profit)
        result.append({"average_profit": round(average_profit)})
    json.dump(result, write_f)