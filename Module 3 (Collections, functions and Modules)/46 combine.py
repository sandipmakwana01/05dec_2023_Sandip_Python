"""Write a Python program to combine values in python list of dictionaries.
Sample a: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})"""

from collections import Counter

def combine(x):
    n = Counter()

    for d in x:
        item = d['item']
        amount = d['amount']
        n[item] += amount
    return n

a = [{'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}]

b = combine(a)
print("Expected Output:")
print(b)
