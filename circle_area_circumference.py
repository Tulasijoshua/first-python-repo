class Circle:
    pi = 3.14
    def __init__(self, circle_radius):
        self.radius = circle_radius

    def areaOfCircle(self):
        area = Circle.pi * self.radius**2
        return area
    def circumOfCircle(self):
        circumference = 2 * self.pi * self.radius
        return circumference

area_1 = Circle(4)
print(area_1.areaOfCircle())
print(area_1.circumOfCircle())