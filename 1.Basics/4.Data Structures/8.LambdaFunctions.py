items = [
    ("Product_1", 15),
    ("Product_3", 10),
    ("Product_2", 5)
]

# items.sort(key=lambda parameters:expression)
items.sort(key=lambda item:item[1])
print(items)
# [('Product_2', 5), ('Product_3', 10), ('Product_1', 15)]
