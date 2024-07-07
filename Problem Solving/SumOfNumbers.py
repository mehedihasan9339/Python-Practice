def sum_of_numbers(n):
    total = 0

    for num in range(1, n + 1):
        total += num
    return total

#Test the function
print(sum_of_numbers(5)) #Output: 15
print(sum_of_numbers(3)) #Output: 6
