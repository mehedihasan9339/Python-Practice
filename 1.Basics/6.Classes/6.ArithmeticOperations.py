class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


point = Point(10, 20)
other = Point(1, 2)
print(point + other)
# <__main__.Point object at 0x000002BC21515E50>

combined = point + other
print(f"({combined.x}, {combined.y})") # (11, 22)

difference = point - other
print(f"({difference.x}, {difference.y})") # (9, 18)

