class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)

other = Point(1, 2)
# '==' compares two objects in memory so your not comparing
# the values or contents of the objects when using '==' on
# complex objects, instead use a comparison magic method
# for comparing two objects.
#print(point == other)

#
print(point > other)
