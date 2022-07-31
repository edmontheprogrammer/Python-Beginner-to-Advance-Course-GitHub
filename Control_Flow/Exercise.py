# Write a program that displays even numbers between 1 to 10 
counter = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        counter += 1
print(f"There are {counter} even numbers")