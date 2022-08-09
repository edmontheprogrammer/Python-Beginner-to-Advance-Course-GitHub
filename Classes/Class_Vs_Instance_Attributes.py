# Instance Attributes; x y and z are instance attributes.
# x, y and z belong to the point instances or point objects
# so that every point object can have different values for these
# attributes.
# objects in Python are dynamic
class Point:
    # 'default_color' is a class level attribute
    # class attributes can be read via a class reference or object
    # reference
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# Using a class reference
Point.default_color = "yellow"

point = Point(1, 2)
# Example of using 'class object' to read  'class level attribute',
# 'default_color'
print(point.default_color)
# Example of using the class name  to read 'class level attribute',
# 'default_color'
print(Point.default_color)

# Note 1: Class attributes are shared across all instances of a class
# meaning when you create a new object of a class, the attributes
# that gets defined at a class level will be available to all
# objects. Each object can modify the values of attributes that are
# created at 'the class level'

# z is an instance attribute that belongs to the point object.
# point.z = 10
# point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()


# Class attributes; attributes that we define at the class level.
# Class attributes are the same across all instances of the class.
# Attributes that get shared among all instances.
# For example, all humans have two eyes and two ears, 'eyes' and 'ears'
# would be attributes that we define at the class level since
# they are attributes that all humans must have. On the other hand,
# 'instance attributes' are attributes that belong to a specific human
# such as 'private jet', not every human has a privete jet only a few,
# therefore 'private jet' is an example of an 'instance attribute' that
# can only belong to specific humans  like 'Bill Gates' and 'Mark Cuban'

# Use instance attributes or variables most of the time to
# minimize logical errors from multiple methods changing value of
# the same variable, be aware of class attributes and
# when they can be useful.
