items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# filter() is a built-in method that allows us to filter list items
# For example, use the filter() function to only get values of items with
# prices greater than 10 dollars
# filter() function works similar to the map() function, takes two parameters
# 'function' and 'iterable object'.
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
