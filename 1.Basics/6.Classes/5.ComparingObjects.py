class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def draw(self):
        print(f"Point({self.x}, {self.y})")

point = Point(2, 3)
other = Point(2, 3)

print(point == other) # True

point = Point(20, 30)
print(point > other) # True


point = Point(1, 2)
print(point < other) # True
