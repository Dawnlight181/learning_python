class Hexagon:
    def __init__(self, side1, side2, side3, side4, side5, side6):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.side5 = side5
        self.side6 = side6
        print("Created!")

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

hexagon1 = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon1.calculate_perimeter())
