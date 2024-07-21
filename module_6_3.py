class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

    def voice(self):
        print(Eagle.sound)


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)


def get_pos():
    return Horse.x_distance, Eagle.y_distance
    super().voice()


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
