items = [
    ("Product_1", 15),
    ("Product_3", 10),
    ("Product_2", 5)
]

prices = []
for item in items:
    prices.append(item[1])

print(prices) # [15, 10, 5]

x = map(lambda item:item[1], items)

print(x) # <map object at 0x000001F8A7F35CF0>

for item in x:
    print(item)

# 15
# 10
# 5

price_list = list(map(lambda item:item[1], items))
print(price_list) # [15, 10, 5]
