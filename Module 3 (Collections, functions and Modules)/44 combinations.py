"""Write a Python program to create and display all b of letters,
selecting each letter from a different key in a x.
Sample a: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd"""

from itertools import product

def combinations(x):

    m = [
        x[key] 
        for key in sorted(x.keys())
        ]

    n = list(product(*m))

    p = [
        ''.join(o) 
        for o in n
        ]

    return p

a = {'1': ['a', 'b'], '2': ['c', 'd']}

b = combinations(a)

print("Expected Output:")
print(' '.join(b))
