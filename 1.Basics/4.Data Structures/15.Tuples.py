point1 = 1, 2
print(type(point1)) # <class 'tuple'>

point2 = (2, 3)
print(type(point2)) # <class 'tuple'>

print(point1 + point2) # (1, 2, 2, 3)
print(point1 * 3) # (1, 2, 1, 2, 1, 2)

print(tuple("Hello")) # ('H', 'e', 'l', 'l', 'o')

print(point1[0:2]) # (1, 2)

x, y = point2
print(y) # 3

if 2 in point2:
    print("exists") # exists
