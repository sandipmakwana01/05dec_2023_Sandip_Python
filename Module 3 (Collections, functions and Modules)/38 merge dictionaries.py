"""Write a Python script to merge two Python dictionaries"""

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

m = d1.copy()
m.update(d2)

print("Merged Dictionary:", m)

