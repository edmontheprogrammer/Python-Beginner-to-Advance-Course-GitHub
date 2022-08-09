# An Abstract Base Class is like a half baked cookie, it's not ready
# to be eaten, if it's baked, it's half cooked, it's purpose is
# provide some common code to these derivities. So we want to the
# 'Steam' class an abstract base class.
# Creating Abstract classs:
# Step 1: Import these into the python file 'from abc import ABC, abstractmethod'
# Step 2: To make the 'Stream' class we defined an abstract class,
# we make it inherit from the 'ABC' class.
# Step 3: Define all the common methods for all the 'sreams' or
# the classes that will inherit the features of the 'Stream' class.
# Then add the 'abstractmethod' method decrator to tell Python that
# this method is an abstract method.
# Note 1; When a class has an abstract method, it considered an
# abstract class. Which means we cannot instantiate them or
# create an object of them. We cannot create an instance of the
# 'Stream' class below because the method 'read()' is defeind as
# an abstract method when we added 'abstractmethod' decroter on
# top of it. (ABC) and 'abstractmethod' made the entire 'Stream'
# class an abstract class.

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    # Implenting the read() method as an abstract method using the
    # '@abstractmethod' decroter
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class Network(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")


stream = MemoryStream()
stream.open()
