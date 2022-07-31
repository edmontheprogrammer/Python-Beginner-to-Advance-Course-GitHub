# numbers = [3, 51, 2, 8, 6]
# numbers.sort()
# # sort() ---> sorts items from smallest to largest
# # sort() changes the order of values in the original list
# print("numbers list in order:")
# print(numbers)
# # sort() ---> takes keywords argument to change the
# # the order of sorting 'reverse=True' largest to smallest

# print("numbers list in reverse order:")
# # numbers.sort(reverse=True)
# # print(numbers)

# # sorted() --> method that takes iterable as input
# # parameter and returns a new list in ascending order
# # The original list isn't being changed when using sorted()
# # method since it returns a new list or different list
# # sorted() method can also take input parameters to change
# # the order of the iterable being passed in such as 'reverse=True'
# print("numbers list being sorted using sorted() method:")
# sorted(numbers, reverse=True)
# print(numbers)

# Create a method when sorting complex objects other
# than primitive data types
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# sorting the items list of tuples
# Step 1: Create a method, sort_item()
# Step 2: access indivisual item in the list
# being passed in such as 'item[1]', gives us
# a tuple "('Products', 9)" the first item in the
# items list above.
# Note 1: items' list contains 'list of tuple objects',
#  so it's a list of lists.  'item[0]' gives us
# '("Product1", 10)' and 'item[1]' gives us
# '("product2", 9)'
# Note that sort_item() method is now a function that
#  can return indivisual item of any list or iterable
# object.
# Step 3:


def sort_item(item):
    return item[1]


# x = sort_item(items)
# print(x)

# sorting the 'items' list
# sort() method takes input parameter,
# first parameter is key, passing a reference to
# "sort_item" function
# Note 2, sort() takes 'sort_item' method
# as the keyword argument
items.sort(key=sort_item)
print(items)
