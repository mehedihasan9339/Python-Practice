fruits = ["apple", "mango", "cherry"]
print(fruits)

#Accessing elements
print(fruits[0])
print(fruits[1])

#Adding elements
fruits.append("date")
print(fruits)

#Remove an element
fruits.remove("mango")
print(fruits)

#Get and remove the last item
print(fruits.pop())

#Get the index position of an item in the array
print(fruits.index("apple"))