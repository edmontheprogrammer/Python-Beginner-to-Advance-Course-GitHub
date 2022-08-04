value1 = []
for x in range(5):
    value1.append(x * 2)
# Comprehesions List: for each 'item' in the 'items' list, get each 'item'
# and perform the 'expression' on that 'item'
# [expression for item in items]

# Comprehesions List are not just limited to 'list data type'
# You can use list comprehesions with sets and dict.
values2 = {x: x * 2 for x in range(5)}
# What's the difference between dict's syntax and set's syntax?
# set has single values with braces
{1, 2, 3, 4}
# dict. has values separted by colon
{1: "a", 2: "b"}
# print(values2)

# working with tuples
values3 = (x * 2 for x in range(5))
print(values3)  # returns a genererator object, not a tuple
