# Animal: Parent, Base

# All Class inherits from the default class `object`
# class Animal(object):
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

print(isinstance(m, Mammal)) # True
print(isinstance(m, Animal)) # True
print(isinstance(m, object)) # True
print(isinstance(m, Fish)) # False
