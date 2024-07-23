class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point (x: {self.x}, y: {self.y})")


point = Point(1, 2)
print(point.y) # 2
point.draw() # Point (x: 1, y: 2)

another = Point(3, 4)
another.draw() # Point (x: 3, y: 4)