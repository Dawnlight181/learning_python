class Person:
    def __init__(self):
        self.name = 'Bob'

    def print_bob(self):
        print(self)
        
bob = Person()
same_bob = bob
print(bob is same_bob)


another_bob = Person()
print(bob is another_bob)
