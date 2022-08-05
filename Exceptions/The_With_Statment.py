try:
    with open("app.py") as file, open("another.txt") as target:
        print("File Open.")
        file.__exit__
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
