letters = ["a", "b", "c"]

print(letters.count("d")) # 0
print(letters.count("c")) # 1

key_letter = "c"
if key_letter in letters:
    index_position = letters.index(key_letter)
    print(f"index position of '{key_letter}' is {index_position}")
else:
    print("Not Found")

# index position of 'c' is 2
