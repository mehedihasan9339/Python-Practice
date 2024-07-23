# Class: blueprint for creating a new objects
# Object: instance of a class

# Class: Human
# Objects: Jogn, Marry, Jack

class Point:
    def draw(self):
        print(f"draw {self}")


point = Point()
print(type(point)) # <class '__main__.Point'>
print(isinstance(point, Point)) # True
print(isinstance(point, int)) # False

