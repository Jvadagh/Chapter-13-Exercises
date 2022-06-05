"""
7. Given the definition of the geometric Point class, add a method named distance:
"""
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def doubledistance(self, p):
        d = math.sqrt((a.x - p[0]) ** 2 + (a.y - p[1]) ** 2)
        return d


if __name__ == '__main__':
    a = Point(2, 3)
    print(a.doubledistance((3, 3)))
