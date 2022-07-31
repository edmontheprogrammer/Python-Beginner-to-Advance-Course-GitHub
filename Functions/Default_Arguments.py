# All optional or Default parameters must come after the 
# required parameters, 'number' is a required parameter
def increment(number, by=1):
    return number + by


# keyword arguments are keywords that that repersent names for 
# function parameters when you call them 
print(increment(2, 5))