from sys import getsizeof

values = (x * 2 for x in range(10000))
print(values) # <generator object <genexpr> at 0x000001FD45FEC520>

print("gen: ", getsizeof(values)) # gen:  200

# print(len(values))
# object of type 'generator' has no len()

values = [x * 2 for x in range(50)]
print("list: ", getsizeof(values)) # list:  472

