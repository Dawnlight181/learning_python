class Apple:
    def __init__(self, w, c, f, s):
        self.weight = w
        self.color = c
        self.form = f
        self.sugar_content = s
        print("Created!")

apple1 = Apple(10, "red", "circle", 89)
print(apple1.color)
print(apple1.weight)
print(apple1.form)
print(apple1.sugar_content)
