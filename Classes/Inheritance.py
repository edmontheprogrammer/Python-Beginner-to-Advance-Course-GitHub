# Inheritance is a mechanism that allows us to define the common
# behavior or common functions in one class, and then inherit them in
# other classes.

class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# The mammal class is an animal becuase it inherits all the functions of
# the Animal class. Animal is the Base class and Mammal is the
# subclass.
class Mammal(Animal):
    def walk(self):
        print("wallk")


class Fish(Animal):

    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
