numbers = [1, 1, 2, 3, 4]
first = set(numbers)

print(first) # {1, 2, 3, 4}

second = {1, 2, 3}
second.add(5)
second.remove(2)

print(len(second)) # 3
print(second) # {1, 3, 5}



# first = {1, 2, 3, 4}
# second = {1, 3, 5}

# union
print(first | second) # {1, 2, 3, 4 ,5}

# intersection
print(first & second) # {1, 3}

print(first - second) # {2, 4}
print(first ^ second) # {2, 4, 5}

if 1 in first:
    print("exists") # exists
