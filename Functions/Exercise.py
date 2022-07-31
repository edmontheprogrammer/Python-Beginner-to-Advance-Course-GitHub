def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        print("Fuzz Buzz") 
    elif input % 3 == 0:
        print("Fuzz")
    elif input % 5 == 0:
        print("Buzz")
    else:
        print(f"{input}")

print(fizz_buzz(127))

# Second Method 

def fizz_buzz_2(input):
    if input % 3 == 0: 
        result = "Fizz"
    else:
        result = "Buzz"
    return result

print(fizz_buzz_2(5))

# Third Method
def fizz_buzz_3(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizz Buzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
    
print(fizz_buzz_3(24))