# A lambda functions is a small anonymous function.
# A lambda function can take any number of arguments, but
# can only have one expression
# lambda arguments : expression
# Example, Here, 'x' is our lambda function, we use the keyword 'lambda'
# to define the lambda function, 'a' is the argument giving to the lambda
# function and 'a + 10' is the expression giving to the lmabda function,
# 'a + 10' is the experssion lambda will compute.
def x(a):
    return a + 10


print(x(5))


# x(5) is calling the lambda function normally and we are passing
# '5' as the argument that will be assigned to 'a'. Then the expression
# 'a + 10' gets evaluated and the the lmabda expression 'a + 10' will be
# returned from the function.
items = [
    ("Products1", 10),
    ("Products", 9),
    ("Products3", 12)
]
# def sort_item(item):
#     return item[1]

items.sort(key=lambda item: item[1])
print(items)
