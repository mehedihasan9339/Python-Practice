from array import array

numbers = array('i', [1, 2, 3])

print(numbers.index(3)) # 2

numbers[2] = 4

print(numbers) # array('i', [1, 2, 4])


numbers[2] = 4.0
print(numbers)

#TypeError: 'float' object cannot be interpreted as an integer