"""How can you pick a random item from a range?"""
import random

a = 1
b = 10

c = random.choices(range(a,b))

print("Random item from the range:", c)
