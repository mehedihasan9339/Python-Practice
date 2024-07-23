letters = ["a", "b", "c", "d", "e"]

print(letters[0]) # a
print(letters[-1]) # e
print(len(letters)) # 5

letters[0] = "A"
print(letters) # ['A', 'b', 'c', 'd', 'e']

print(letters[0:3]) # ['A', 'b', 'c']
print(letters[3:]) # ['d', 'e']
print(letters[::2]) # ['A', 'c', 'e']

numbers = list(range(10))
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::2]) # [0, 2, 4, 6, 8]
print(numbers[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]