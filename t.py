class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("Created!")

    def area(self):
        return self.base * self.height / 2
    
triangle1 = Triangle(5, 8)
print(triangle1.area())
