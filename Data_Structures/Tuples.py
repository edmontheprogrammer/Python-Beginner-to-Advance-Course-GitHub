# Tuples --> read only list, immutable
# define a tuple
point1 = 1, 2
print(type(point1))

single_tuple_value = 1,  # remember to add comma ',' at the end of the value
# else it becomes an integer
intger_value = 1

# empty tuple are defined using empty ()
empty_tuple = ()

# adding two tuples
point2 = (1, 2) + (3, 4)
print(point2)  # outputs (1, 2, 3, 4) similar to list [1, 2, 3, 4] but
# type is <class 'tuple'>
print(type(point2))

point3 = (1, 2) * 3  # repeats a tuple
print(point3)

# convert list to tuple using the built-in tuple() function that
# takes iterable
point4 = tuple([1, 2])

# tuple of strings
point5 = tuple("Hello World")
print(point5)

# accessing tuple items
point6 = (1, 2, 3)
print(point6[1])
print(point6[0:2])

# unpacking tuple
x, y, z = point6
print(x)
print(y)
print(z)

# checking for item in tuple
if 10 in point6:
    print("exists")

# Remember that tuples are immutable, they cannot be changed like lists
point6[0] = 10
# Therefore, tuple does NOT have built-in functions like append(), pop()
