items = [
    ("Product_1", 15),
    ("Product_3", 10),
    ("Product_2", 5)
]

x = filter(lambda item:item[1] >= 10, items)
print(x) # <filter object at 0x0000013CC7475B40>

filtered_list = list(filter(lambda item:item[1] >= 10, items))
print(filtered_list) # [('Product_1', 15), ('Product_3', 10)]

