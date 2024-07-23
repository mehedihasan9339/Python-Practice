def save_user(**user):
    print(user["name"])
    print(user)

save_user(id = 1, name = "Mr X", age = 30)

# Mr X
# {'id': 1, 'name': 'Mr X', 'age': 30}
