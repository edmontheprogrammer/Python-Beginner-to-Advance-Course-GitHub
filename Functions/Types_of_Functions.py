def greet(first_name, last_name):
    print()

print(greet("Sarah", "Thomas"))
# greet() is a function that returns 'None'
# In Python, all functions returns a type of 'None' by default

# Two types of functions
# 1 - Perform a task 
# 2 - Returns a value 
# Which function type is better? 
# number 2

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Tim")
print(message)
# file = open("content.txt", "w")
# file.write(message)

