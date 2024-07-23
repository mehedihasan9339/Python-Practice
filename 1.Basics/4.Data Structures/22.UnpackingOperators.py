first = [1, 2]
second = [3]

values = [*first, "a", *second, "Hello"]
print(values) # [1, 2, 'a', 3, 'Hello']

values = [*first, "a", *second, *"Hello"]
print(values) # [1, 2, 'a', 3, 'H', 'e', 'l', 'l', 'o']

first = {"x": 1}
second = {"x": 10, "y": 20}
combined = {**first, **second, "z": 1}
print(combined) # {'x': 10, 'y': 20, 'z': 1}

