numbers = [1, 2, 3, 4]
first, second, third, last = numbers

print(first, last) # 1 4

first, second, *other = numbers
print(first) # 1
print(other) # [3, 4]

for number in other:
    print(number)

# 3
# 4

first, *other, last = numbers
print(other) # [2, 3]
print(last) # 4
