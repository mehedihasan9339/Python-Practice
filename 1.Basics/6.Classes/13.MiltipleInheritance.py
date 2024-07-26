class Employee():
    def greet(self):
        print("Employee Greet")


class Person():
    def greet(self):
        print("Person Greet")

class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet() #Two methods, Calls the first one (Employee Greet)




class Flyer():
    def fly(self):
        print("fly")


class Swimmer():
    def swim(slef):
        print("swim")

class FlyingFish(Flyer, Swimmer):
    pass

flyingfish = FlyingFish()
flyingfish.fly() # fly
flyingfish.swim() # swim
