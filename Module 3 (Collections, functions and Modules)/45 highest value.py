"""Write a Python program to find the highest 3 values in a dictionary"""

import heapq

a = {'a': 10, 'b': 30, 'c': 20, 'd': 25, 'e': 15}
n=3

x = heapq.nlargest(n,a.values())
print("Highest 3 Values:", x)
