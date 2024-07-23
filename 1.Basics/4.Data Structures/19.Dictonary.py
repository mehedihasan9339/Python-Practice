point = {"x": 1, "y": 2}
print(point) # {'x': 1, 'y': 2}

point = dict(x = 1, y = 2)
print(point) # {'x': 1, 'y': 2}

point["x"] = 10
print(point) # {'x': 10, 'y': 2}

point["z"] = 20
print(point) # {'x': 10, 'y': 2, 'z': 20}

if "a" in point:
    print(point["a"])
else:
    print(point.get("a"))

#None

del point["x"]
print(point) # {'y': 2, 'z': 20}

for key in point:
    print(key)

# y
# z

for item in point.items():
    print(item)

# ('y', 2)
# ('z', 20)


for key, value in point.items():
    print(key, value)

# y 2
# z 20
