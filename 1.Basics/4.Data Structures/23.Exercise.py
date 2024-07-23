# find the character frequencies in a given sentence
from pprint import pprint

sentence = "Python Programming"

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)
# {'P': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}

pprint(char_frequency, width=1)
# {' ': 1,
#  'P': 2,
#  'a': 1,
#  'g': 2,
#  'h': 1,
#  'i': 1,
#  'm': 2,
#  'n': 2,
#  'o': 2,
#  'r': 2,
#  't': 1,
#  'y': 1}

sorted_frequency = sorted(char_frequency.items(), key = lambda value:value[1], reverse = True)
print(sorted_frequency)
# [('P', 2), ('o', 2), ('n', 2), ('r', 2), ('g', 2), ('m', 2), ('y', 1), ('t', 1), ('h', 1), (' ', 1), ('a', 1), ('i', 1)] 

print(f"most used character is: {sorted_frequency[0]}")
# most used character is: ('P', 2)

print(f"most used character is: {sorted_frequency[0][0]}, {sorted_frequency[0][1]} times")
# most used character is: P, 2 times
