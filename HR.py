class Horse:
    def __init__(self, speed, color, size, owner):
        self.speef = speed
        self.color = color
        self.size = size
        self.owner = owner

class Rider:
    def __init__(self, name, sex, height):
        self.name = name
        self.sex = sex
        self.height = height

shiryu = Rider("Shiryu Takahashi", "male", 170)
mickky = Horse("fast", "white", "big", shiryu)
print(mickky.owner.name)
