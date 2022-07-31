letters = ["a", "b", "c"]
# Add
# append() --> end of the list
letters.append("d")
# insert() --> specific location in the list
letters.insert(0, "-")

# Remove
letters.pop()
# remove() first occurance of a value from the list
letters.remove("b")
# removing occurance of every item in the list ---> loop
del letters[0:3]
# removing all the items in the list --> clear()
print(letters)
