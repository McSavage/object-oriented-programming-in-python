from math import pi

class circle:
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return pi*self.radius*self.radius

    @property
    def diameter(self):
        return self.radius*2

    @property
    def circumference(self):
        return pi*self.radius*2

    def display(self):
        print(self.radius, self.diameter, self.circumference, self.area())
