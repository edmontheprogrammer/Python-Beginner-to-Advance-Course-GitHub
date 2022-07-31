message = "a" # scope of global variables are the entire file
# Avoid using global variables when you can
def greet(name):
    # Bad practice when multiple functions change a value of global variables
    global message
    # Scope of message here is local, local to the greet function
    message = "b"


greet("Walter")
print(message)