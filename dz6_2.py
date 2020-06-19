class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        print(f"The mass of asphalt, kg: {self._length * self._width * 25 * 5}")

def enter():
    while True:
        try:
            road = Road(float(input("Enter the width of the road, m: ")), float(input("Enter the length of the road, m: ")))
            road.calc()
            break
        except ValueError:
            print("You have enter only numbers")

enters = enter()