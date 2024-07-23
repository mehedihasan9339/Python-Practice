list1 = [1, 2, 3]
list2 = [10, 20, 30]

zipped = zip(list1, list2)
print(zipped) # <zip object at 0x0000023EA92E3AC0>

for item in zipped:
    print(item)

# (1, 10)
# (2, 20)
# (3, 30)

print(list(zip("abc", list1, list2)))
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]

print(list(zip("ab", list1, list2)))
# [('a', 1, 10), ('b', 2, 20)]
