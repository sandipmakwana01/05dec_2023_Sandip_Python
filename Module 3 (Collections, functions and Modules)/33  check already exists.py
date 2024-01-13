"""Write a Python script to check if a given key already exists in a dictionary."""
def check(dictionary, key):
    return key in dictionary

a = {'a': 1, 'b': 2, 'c': 3}
b = 'b'

result = check(a, b)

if result:
    print(f"The key '{b}' exists in the dictionary.")
else:
    print(f"The key '{b}' does not exist in the dictionary.")
