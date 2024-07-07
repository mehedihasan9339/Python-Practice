def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Test the function
print(is_leap_year(2020))  # Output: True
print(is_leap_year(2021))  # Output: False
print(is_leap_year(2000))  # Output: True
print(is_leap_year(1900))  # Output: False
