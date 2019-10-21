class Square:
    def __init__(self, side):
        self.side = side

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

s1 = Square(8)
print(s1)
