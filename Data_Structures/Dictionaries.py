# Used to map a key to a value
# like phone book name -> contact phone number
# string for key and integer for value
# Define a dictionary using braces
from multiprocessing.sharedctypes import Value


point1 = {"x": 1, "y": 2}
# Define a dictionary using Python's built-in "dict()" function
# and pass keyword arguments (variable_name = variable_value)
# keyword argument "x = 1"
point2 = dict(x=1, y=2)
# Get dictionary value using index.
# Dict index is a name of the key.
dict_value = point2["x"]
print(dict_value)
# Changing value at index 'x'
point2["x"] = 10
# Adding new key to the point2 dictionary
point2["z"] = 20
print(point2)
# Key error 'a'
# print(point2["a"])
if "a" in point2:
    print(point2["a"])
print(point2.get("a", 0))
# delete item from dictionary
del point2["x"]
print(point2)
print("Looping over Dict. method # 1----------------")
# Looping over dict method # 1
for key in point2:
    print(key, point2[key])
print("Looping over Dict. method # 2----------------")
# returns a tuple and you can unpack it in the for-loop
for key, value in point2.items():
    print(key, value)
