# Arrays more efficient than list data type in Python
#  for large data set greater than 100,000 and have performance issues.
# Else use 'lists' and 'tuples' by default
from array import array

# Using Python array requires type code.
# Type code specifiy the type of values array will store.
# https://docs.python.org/3/library/array.html
# 'i' type code unsigned int (C Type), Python int (Python Type)
numbers = array("i", [1, 2, 3])
# array have similar built-in functions like lists such as "remove()"
# Unlike 'lists', objects in Python array is 'typed' base.
# Cannot mix 'strings', 'integer', 'list' in Python arrays.
# Python arrays similar to arrays in the C language.
# numbers[0] = 1.0  # results in TypeError


[1, 2, 3]  # define list
