try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    file.close()
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No execptions were thrown.")
finally:
    file.close()
