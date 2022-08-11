# Data Classes; the concept of data classes is to create classes
# that don't have any behaviors or methods. They only have data,
# those data are repersented by variables and data structures like
# integer variables being initialized to a value and list data type
# with a list of values such as strings.

# Simply creating a class named 'Point' with an '__init__()' method
# that takes two input parameters 'x' and 'y', 'x' and 'y' get initialize
# using 'self.x' and 'self.y'.


from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Creating two Point objects, p1, p2
p1 = Point(1, 2)
p2 = Point(1, 2)
# p1 is not equal to p2 because they are stored in different places in
# memory. You'll need to implement magic method '__eq__()'
# print(p1 == p2)
# 'id()' is a built-in method that returns the memory address of where
# an object is stored.
# print(id(p1))
# print(id(p2))

# Also, you can use 'namedtuple'.
# If you're dealing with classes that have no behavior, no methods,
# they only have data, you can use a 'namedtuple' instance
# Remeber that tuple is an immutable data type, you cannot modify
# the values
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
# p1.x = 10  # results in error, AttributeError: can't set attribute
p2 = Point(x=1, y=2)
print(p1 == p2)
