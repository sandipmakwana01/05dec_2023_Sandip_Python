"""Write a Python function that takes a list and returns a new list with unique
elements of the first list."""

def unique(x):
    b = list(set(x))
    return b

a = [1, 2, 2, 3, 4, 4, 5]
unique(a)

print("Original List:", a)
print("List with Unique Elements:", unique(a))
