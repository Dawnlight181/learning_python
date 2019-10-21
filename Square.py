class Square:
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

s1 = Square(9)
s2 = Square(8)
s3 = Square(5)
print(Square.square_list)
