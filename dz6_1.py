from time import sleep


class Trafficlight:
    __color = 0

    def running(self):

        lights = [
            {'name': 'red', 'color': '\x1b[41m', 'delay': 5},
            {'name': 'yellow', 'color': '\x1b[43m', 'delay': 2},
            {'name': 'green', 'color': '\x1b[42m', 'delay': 5},
        ]

        print('\nSimple trafficlight:\n')

        while True:
            s = ''
            for i in range(3):
                if i == self.__color:
                    s += f'({lights[self.__color]["color"]} \x1b[0m)'
                else:
                    s += '( )'

            print(f'\r{s}', end='')

            sleep(lights[self.__color]["delay"])

            self.__color = (self.__color + 1) % 3


lights = Trafficlight()
lights.running()
