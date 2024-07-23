successfull = False

for number in range(3):
    print("Attempt", number + 1)
    if successfull:
        print("Successfull")
        break
else:
    print(f"Attempts {number + 1} times and failed")

# Attempt 1
# Attempt 2
# Attempt 3
# Attempts 3 times and failed