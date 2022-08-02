# The 'map()' function executes a specified function for each item in
# an iterable. The item is sent to the function as a parameter
# Syntax: map(function, iterable)
# parameter 'function'; requried. The function to execute for each item
# Parameter 'iterable': Required. A sequence, collection or an iterator object
# You can send as many iterables as you like, just make sure the function
# haas one parameter for each iterable.
# Example,
# Make new fruits by send two iterable object into the function:
def myfunc(a, b):
    return a + b


y = map(myfunc, ('apple', 'banana', 'cherry'),
        ('orange', 'lemon', 'pineapple'))


# list of tuple data type
items = [
    ("Products1", 10),
    ("Products", 9),
    ("Products3", 12)
]

# # Creating an empty list
# prices = []
# # Creating a for-in to loop over the list items and append the
# # 'item' value, tuple value, the empty list, 'prices'
# for item in items:
#     prices.append(item[1])
# Note: the 'map()' function returns an iterable object, you can
# can easily loop over it like a list. We pass the iterable object
# being returned by the map function to the 'list()' function

x = list(map(lambda item: item[1], items))

# Ouput 'prices' list which returns all the values of the list items' 'item'!
# Simply all the values of the tuple data type stored in items' list
print(x)
