class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx


class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return f'({self.x_distance}, {self.y_distance})'

    def voice(self):
        print(f'{self.sound}')


p1 = Pegasus()
p2 = Pegasus()
p3 = Pegasus()
print()

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

