def switch_example(value):
    if value == 1:
        return "Case 1"
    elif value == 2:
        return "Case 2"
    elif value == 3:
        return "Case 3"
    else:
        return "Default case"

# Test the function
print(switch_example(1))  # Output: Case 1
print(switch_example(2))  # Output: Case 2
print(switch_example(4))  # Output: Default case
