# Set is a collection with no duplicate values
# Set is a data stucture that does not allow repeated values
# Implment set data structure using Python's built-in 'set()' function
# Sets are defined using braces, {}, similar to Python dictionary
# but the values in sets are 'list' of values. On the other hand,
# dictionary contains key-value pairs.
# The set collection, data structure, has similar methods to the
# list data structure such as 'add()', 'remove()' and 'len()'
numbers = [1, 1, 2, 3, 4]
first_set = set(numbers)
print(first_set)
second_set = {1, 5}
second_set.add(5)
second_set.remove(5)
len(second_set)
# Sets are more useful in math operations
# Union operation, two sets
union_value = first_set | second_set
# returns unique values in first set or second set
print("union value: ", union_value)
# Intersection of two sets
intersection_value = first_set & second_set
print("intersection value: ", intersection_value)
# Difference between two sets
difference_value = first_set - second_set
print("difference value: ", difference_value)
# Semantic difference, returns values that either in
# first_set or second set, but not both sets
sematic_value = first_set ^ second_set
# Unlike list, items in sets are unordered (not in order)
# print(first_set[0])
# Trying to access index of a set returns error because items in set
# are not in order
#  ---> TypeError: 'set' object is not subscriptable
# Use a list to access value items, instead of trying to 
# access values of set by index
if 1 in first_set:
    print("yes")
