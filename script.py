import math


class Punto2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_distance_two_points(x1, y1, x, y):
    dx = (x1 - x)**2
    dy = (y1 - y)**2
    return math.sqrt(dx + dy)


mi_punto = Punto2d(4, 0)

print(get_distance_two_points(mi_punto.x, mi_punto.y, 2, 2))
