message = "a"

def greet(name):
    print(f"Hello {name}")
    global message
    message = "b"

greet("Mehedi")
print(message)

# Hello Mehedi
# b (global variable has changed!)