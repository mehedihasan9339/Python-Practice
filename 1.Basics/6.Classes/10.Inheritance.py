# Animal: Parent, Base
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Mammal: Child, Sub

class Mammal(Animal):
    def walk(self):
        print("walk")

# Fish: Child, Sub
class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat() # eat
print(m.age) # 1
