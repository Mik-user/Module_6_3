class Horse:
    sound = 'Frrr'
    x_distance = 0
    def __init__(self):
        super().__init__()

    def run(self, dx):
        self.run = self.x_distance+dx
        self.x_distance = self.run


class Eagle:
    y_distance = 0
    def __init__(self):
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.fly = self.y_distance + dy
        self.y_distance = self.fly
class Pegasus(Horse,Eagle):
    def __init__(self):
        super().__init__()
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
    def get_pos(self):
        tuple_= (self.x_distance, self.y_distance)
        return tuple_

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()