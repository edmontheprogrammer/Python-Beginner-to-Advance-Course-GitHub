# In Python we can also use inheritance with the built in types.
# For example, this 'Text' class takes 'str' as parameter
# which gives 'Text' all the features and functions of Python 'str'.
# We can also add additional features to it in our class
class Text(str):
    def duplicate(self):
        return self + self


# creating a text object, 'text' has all the functions of Python's
# built-in string data type
# text = Text("Python")
# print(text.duplicate())

# Extending the append() method of Python's built-in
# list data structure
class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")
print(list)
