# A property is an object that sits in front of an attribute and allows
# us to get or set the value. These are your getters and setters method
#

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(-10)
product.price = 2
print(product.price)
