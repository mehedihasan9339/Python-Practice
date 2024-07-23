# if the input is divisible by 3 then return 'Fizz'
# if the input is divisible by 5 then return 'Buzz'
# if the input is divisible by both 3 & 5 then return 'FizzBuzz'
# Otherwise return the input

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(9))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(11))

# Fizz
# Buzz
# FizzBuzz
# 11