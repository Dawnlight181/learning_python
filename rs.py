class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width + self.len) * 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, new_size):
        self.side += new_size
        
a_rectangle = Rectangle(8, 9)
a_square = Square(7)
print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())
a_square.change_size(200)
print(a_square.calculate_perimeter())
a_rectangle.what_am_i()
a_square.what_am_i()
