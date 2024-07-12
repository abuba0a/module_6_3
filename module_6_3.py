class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self, x_distance, sound):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        Horse.x_distance += dx

    def voice(self):
        print(Horse.sound)


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self, y_distance, sound):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        Eagle.y_distance += dy

    def voice(self):
        print(Eagle.sound)


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance, y_distance):
        super().__init__(Horse.x_distance, Horse.sound)
        super().__init__(Eagle.y_distance, Eagle.sound)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return Horse.x_distance, Eagle.y_distance


p1 = Pegasus(0, 0)
p2 = Pegasus(10, 15)
p3 = Pegasus(5, 5)

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
print()
print(p2.get_pos())
p2.move(5, 10)
print(p2.get_pos())
p2.move(-5, 20)
print(p2.get_pos())
print()
print(p3.get_pos())
p3.move(5, 10)
print(p3.get_pos())
p3.move(-5, 20)
print(p3.get_pos())

p1.voice()

