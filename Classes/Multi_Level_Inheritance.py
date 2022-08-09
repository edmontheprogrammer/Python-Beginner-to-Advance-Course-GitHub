class Animal:
    def eat(self):
        print("eat")

# Multi level inheritance isn't good because it increases the
# complexity of software design.
# Avoid multi level when possible, keep it to one to two levels.


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass
