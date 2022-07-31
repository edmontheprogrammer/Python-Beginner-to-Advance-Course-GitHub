# Variable arguments can also be created using the format **variable_name, 
# '**' follow by 'variable name'. 
# '**variable_name' same as '*variable_name' except '**variable_name'
# returns a dictionary data type {} and '*_variable_name' returns a 
# 'tuple' () data type, both are iterable data structures 
# Double ** asterisks outputs a dictioanry, key-value pair, 
# single asterisk * outputs a tuple
def save_user(**user):
    print(user)

save_user(id=1, name="John", age="22")
