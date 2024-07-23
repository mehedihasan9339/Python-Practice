number = 100
while number > 0:
    print(number)
    number //= 2

# 100
# 50
# 25
# 12
# 6
# 3
# 1

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# >hello
# ECHO hello
# >Python
# ECHO Python
# >Quit
# ECHO Quit