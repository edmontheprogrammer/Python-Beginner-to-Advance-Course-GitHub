# Creating a function that takes a variable number of arguments
# a function that can take a 'collection' number of argument
# Note the variable number of arguments is a 'tuple' data type, 
# 'tuple's are immutable, but iterable

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total 

print(multiply(2, 3, 4, 5))