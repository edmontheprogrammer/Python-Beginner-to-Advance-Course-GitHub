# Instance method are methods that belong to instances of a class
# so when we create a class object, we can call instance methods.
# In this example, '__init__()' and 'draw()' are both instances of
# the 'point' variable, or 'point' object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # example of creating a class method, 'zero'
    # 'zero' is a class method
    # Class methods take 'cls' as first parameter just like instance
    #  method takes 'self' as first parameter
    # 'cls' is short for 'class' and is written by convension 'cls'
    # we can call it anything we want, but stick with 'cls'.
    # We are making a refernce to the 'class' and we are not working
    #  with 'point' objects
    # Finally to make 'zero' a class method. it must be decorated
    # by '@classmethod' keyword also known as a decorator.
    #  This tells Python to make 'zero' a class method.
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# point = Point(0, 0)
# Example of calling a class method 'zero', 'zero' will be a
# method that we defined at the class level
# also 'zero()' is also a factory method, it creates a new object
point = Point.zero()
# example of calling an instance method of the 'point' object
point.draw()
