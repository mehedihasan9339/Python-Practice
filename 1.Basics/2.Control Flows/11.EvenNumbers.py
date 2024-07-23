strat = int(input("start: "))
end = int(input("end: "))

count = 0

for number in range(strat, end + 1):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"There are {count} even numbers")

# start: 1
# end: 10
# 2
# 4
# 6
# 8
# 10
# There are 5 even numbers