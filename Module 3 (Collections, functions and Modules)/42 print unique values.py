"""Write a Python program to print all unique values in a dictionary."""

a = {'a': 100, 'b': 200, 'c': 300, 'd': 200, 'e': 100}
b = set(a.values())
print("Unique Values in the Dictionary:", b)
