course = "Python Programming"
message = """Hi John,
How are you?
I am learning Python Programming!"""
fruit = "apple"

print(course)
print(message)
print(len(course)) #18
print(course[0]) #P
print(course[-1]) #g
print(course[0:3]) #Pyt
print(course[0:]) #Python Programming
print(course[:]) #Python Programming
print(course[1:3]) #yt
print(course[:3]) #Pyt
print(course.title()) #Python Programming
print(course.capitalize()) #Python programming
print(course.lower()) #python programming
print(course.upper()) #PYTHON PROGRAMMING
print(course.index("g")) #10
print(course.find("pro")) #-1
print(course.find("Pro")) #7
print(course.replace("P", "J")) #Jython Jrogramming
print("   Python Programming".strip()) #Python Programming
print("   Python Programming   ".rstrip()) #   Python Programming
print("   Python Programming   ".lstrip()) #Python Programming   
print("Pro" in course) #True
print("c-sharp" not in course) #True

print(fruit[1:-1]) #ppl
print(bool("False")) #True
print(bool("")) #False