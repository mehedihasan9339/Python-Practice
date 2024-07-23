def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

#Test the function
print(factorial(5)) #Output: 120
print(factorial(3)) #Output: 6