try:
    age = int(input("Age: "))
    print(f"Your age is {age}")
except ValueError:
    print("Please enter a valid age.")
else:
    print("No exception thrown")