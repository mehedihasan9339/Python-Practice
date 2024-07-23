numbers = [3, 51, 2, 8, 6]

numbers.sort()
print(numbers) # [2, 3, 6, 8, 51]

numbers.sort(reverse=True)
print(numbers) # [51, 8, 6, 3, 2]

print(sorted(numbers))
print(numbers)

# [2, 3, 6, 8, 51]
# [51, 8, 6, 3, 2]

print(sorted(numbers, reverse=True)) # [51, 8, 6, 3, 2]

items = [
    ("Product_1", 15),
    ("Product_3", 10),
    ("Product_2", 5)
]
items.sort()
print(items)

# [('Product_1', 15), ('Product_2', 5), ('Product_3', 10)]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

# [('Product_2', 5), ('Product_3', 10), ('Product_1', 15)]
