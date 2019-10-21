import math

class Circle:
    def __init__(self, r,):
        self.radius = r
        print("Created!")

    def area(self):
        return self.radius ** 2 * math.pi

circle1 = Circle(4)
print(circle1.area())
