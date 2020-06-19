class Worker:
    def __init__(self, firstn, lastn, position, salary, bonus):
        self.firstn = firstn
        self.lastn = lastn
        self.position = position
        self._salary = salary
        self._bonus = bonus

class Position(Worker):
    def get_full_name(self):
        return f"{self.firstn} {self.lastn}"

    def get_full_income(self):
        return f"{self._salary + self._bonus}"

worker_1 = Position("Andrei", "Shumeiko", "CEO", 500000, 300000)
print(worker_1.get_full_name())
print(worker_1.position)
print(worker_1.get_full_income())