from datetime import date

def days_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days

# Test the function
date1 = date(2024, 1, 1)
date2 = date(2024, 7, 1)
print(days_between_dates(date1, date2))  # Output: 182 (since January 1 to July 1 in 2024)
