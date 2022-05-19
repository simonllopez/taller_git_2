import math


class Punto2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, x, y):
        dx = (self.x - x)**2
        dy = (self.y - y)**2
        return math.sqrt(dx + dy)


mi_punto = Punto2d(4, 0)

print('La distancia es {:.2f}'.format(mi_punto.get_distance(2, 2)))
