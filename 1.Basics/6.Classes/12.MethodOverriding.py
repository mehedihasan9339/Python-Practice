# Animal: Parent, Base
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Mammal: Child, Sub

class Mammal(Animal):
    def __init__(self):
        super().__init__() # Calling Base Class Constructor
        print("Mammal Constructor")
        self.weight = 2


    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)

# Animal Constructor (first called base class constructor)
# Mammal Constructor (then called main class constructor)
# 1 (age)
# 2 (weight)
