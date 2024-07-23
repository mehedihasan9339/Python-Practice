letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5

print(zeros) # [0, 0, 0, 0, 0]

combined = zeros + letters
print(combined) # [0, 0, 0, 0, 0, 'a', 'b', 'c']

numbers = list(range(5))
print(numbers) # [0, 1, 2, 3, 4]

chars = list("Hello World")
print(chars)
print(len(chars))
# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
# 11
