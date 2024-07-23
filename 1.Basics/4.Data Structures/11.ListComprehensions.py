items = [
    ("Product_1", 15),
    ("Product_3", 10),
    ("Product_2", 5)
]

prices = list(map(lambda item:item[1], items))
prices_list = [item[1] for item in items]
print(prices) # [15, 10, 5]
print(prices_list) # [15, 10, 5]

filtered = list(filter(lambda item:item[1] >= 10, items))
filtered_list = [item for item in items if item[1] >= 10]
print(filtered) # [('Product_1', 15), ('Product_3', 10)]
print(filtered_list) # [('Product_1', 15), ('Product_3', 10)]

