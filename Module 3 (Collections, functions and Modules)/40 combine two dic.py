"""Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300})"""

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

a = Counter()

for key in set(d1.keys()) | set(d2.keys()):
    a[key] = d1.get(key, 0) + d2.get(key, 0)

print("Combined Dictionary:", a)
