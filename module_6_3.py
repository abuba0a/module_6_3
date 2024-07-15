class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self):
        self.x_distance = 0

    def run(self, dx):
        Horse.x_distance += dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        self.y_distance = 0

    def fly(self, dy):
        Eagle.y_distance += dy

    def voice(self):
        print(Eagle.sound)


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)


def get_pos():
    return Horse.x_distance, Eagle.y_distance
    super().voice()


p1 = Pegasus()
p2 = Pegasus()
p3 = Pegasus()

print(get_pos())
p1.move(10, 15)
print(get_pos())
p1.move(-5, 20)
print(get_pos())
print()

print(get_pos())
p2.move(5, 10)
print(get_pos())
p2.move(-5, 20)
print(get_pos())
print()
print(get_pos())
p3.move(5, 10)
print(get_pos())
p3.move(-5, 20)
print(get_pos())

p1.voice()
