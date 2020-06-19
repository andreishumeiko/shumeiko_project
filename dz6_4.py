class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'New car: {self.name}, color: {self.color}, police car: {self.is_police}')

    def go(self):
        print(f'{self.name}: The car is in motion')

    def stop(self):
        print(f'{self.name}: The car stopped')

    def turn(self, direction):
        print(f'{self.name}: The car {"turned left" if direction == 1 else "did not change direction"}')

    def show_speed(self):
        return f'{self.name}: The speed of the car: {self.speed}'

class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: The speed of the car: {self.speed}. Excessive speed' \
               if self.speed > 60 else f"{self.name}: The speed of the car {self.speed}"

class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: The speed of the car: {self.speed}. Excessive speed' \
               if self.speed > 40 else f"{self.name}: The speed of the car {self.speed}"

class SportCar(Car):
    pass

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar('NYPD', 'Casual', 100)
police_car.go()
print(police_car.show_speed())
police_car.turn(1)
print()

police_car = TownCar('BMW', 'Black', 100)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)