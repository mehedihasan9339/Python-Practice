from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Test the function
birth_date = date(2000, 5, 15)
print(calculate_age(birth_date))  # Output: Depends on the current date; for 2024, it would be 24
