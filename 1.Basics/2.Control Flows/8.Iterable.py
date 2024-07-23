for x in range(5):
    print(x)

# 0
# 1
# 2
# 3
# 4

for x in "Python":
    print(x)

# P
# y
# t
# h
# o
# n

for x in [1, 2, 3, 4, 5]:
    print(x)

# 1
# 2
# 3
# 4
# 5

shopping_cart = [("product_1", 5), ("product_2", 15), ("product_3", 10)]

for item in shopping_cart:
    print(item)

# ('product_1', 5)
# ('product_2', 15)
# ('product_3', 10)

for item in shopping_cart:
    print(f"product-name: {item[0]}, price: {item[1]}")
    
# product-name: product_1, price: 5
# product-name: product_2, price: 15
# product-name: product_3, price: 10
