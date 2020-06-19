class Stationary:
    def __init__(self, title="The device for drawing"):
        self.title = title

    def draw(self):
        print(f"Just start drawing. {self.title}")

class Pen(Stationary):
    def draw(self):
        print(f"Start drawing with {self.title} pen")

class Pencil(Stationary):
    def draw(self):
        print(f"Start drawing with {self.title} pencil")

class Handle(Stationary):
    def draw(self):
        print(f"Start drawing with {self.title} handle")

stationary = Stationary()
stationary.draw()
pen = Pen("Erich Krause")
pen.draw()
pencil = Pencil("Koh-I-Noor")
pencil.draw()
handle = Handle("Pilot")
handle.draw()