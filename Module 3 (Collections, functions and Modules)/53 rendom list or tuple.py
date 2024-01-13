"""How can you pick a random item from a list or tuple?"""
import random

a = [1, 2, 3, 4, 5]
b = random.choice(a)
print("using list:",b)

c = (1,2,3,4,5)
d = random.choice(c)
print("using tuple:",d)
