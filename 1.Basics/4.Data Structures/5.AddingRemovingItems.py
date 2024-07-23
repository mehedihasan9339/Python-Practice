letters = ["a", "b", "c"]

# Add
letters.append("d")
print(letters) # ['a', 'b', 'c', 'd']

letters.insert(0, "-")
print(letters) # ['-', 'a', 'b', 'c', 'd']

# Remove
letters.pop()
print(letters) # ['-', 'a', 'b', 'c']

letters.pop(0)
print(letters) # ['a', 'b', 'c']

letters.remove("b")
print(letters) # ['a', 'c']

del letters[0:3]
letters.clear()
print(letters) # []
