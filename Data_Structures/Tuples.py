
point1 = 1, 2
print(type(point1))

single_tuple_value = 1,
intger_value = 1


empty_tuple = ()


point2 = (1, 2) + (3, 4)
print(point2)
print(type(point2))

point3 = (1, 2) * 3
print(point3)


point4 = tuple([1, 2])

point5 = tuple("Hello World")
print(point5)

point6 = (1, 2, 3)
print(point6[1])
print(point6[0:2])

# unpacking tuple
x, y, z = point6
print(x)
print(y)
print(z)

if 10 in point6:
    print("exists")

point6[0] = 10
