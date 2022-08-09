# The object class
# Animal: Parent, Base
# Mammal: Child, Sub

class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("wallk")


class Fish(Animal):

    def swim(self):
        print("swim")


m = Mammal()
# isinstance() is a method that tells us if an object is an instance
# of a given class. isinstance() function takes two parameters
# the object of the class your comparing and the name of the
# base class your comparing
print(isinstance(m, Mammal))
