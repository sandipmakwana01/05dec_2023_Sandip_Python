"""Write a Python program to map two lists into a dictionary"""

a = ['a', 'b', 'c']
b = [1, 2, 3]
x = zip(a, b)
y = dict(x)
print("Mapping Dictionary:", y)
