"""
9. Develop a Circle class that, like the Rectangle class above, provides methods to compute perimeter
and area. The Rectangle instance variables are not appropriate for circles; specifically, circles do
not have corners, and there is no need to specify a width and height. A center point and a radius more
naturally describe a circle. Build your Circle class appropriately.
"""


class Circle():
    def __init__(self, radius):
        self.radius = int(radius)

    def perimeter(self):
        p = self.radius * 2 * 3.141
        return p

    def area(self):
        a = self.radius ** 2 * 3.141
        return a


myCircle = Circle(int(input("insert circle radius : ")))
print('perimeter : ', myCircle.perimeter())
print('area : ', myCircle.area())
