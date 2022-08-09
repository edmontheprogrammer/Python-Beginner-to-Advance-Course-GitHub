# Magic methods are methods that have two underscores, '__and__,
# at the beginning and end of their names.
# Magic methods are called automatically by the Python interpreter.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(str(point))
