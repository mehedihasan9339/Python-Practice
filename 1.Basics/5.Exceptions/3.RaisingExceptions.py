def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

# calculate_xfactor(-1) # ValueError: Age cannot be 0 or less.

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# Age cannot be 0 or less.