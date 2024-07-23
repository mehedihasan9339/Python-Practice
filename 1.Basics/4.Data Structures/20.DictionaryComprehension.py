values = []
for item in range(5):
    values.append(item * 2)

print(values) # [0, 2, 4, 6, 8]

values = [item * 2 for item in range(5)]
print(values) # [0, 2, 4, 6, 8]

values = {item: item * 2 for item in range(5)}
print(values) # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

