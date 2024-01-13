"""Write a Python program to check multiple keys exists in a dictionary"""

def check(m, n):
    x = all(
        key in m 
        for key in n
        )
    return x

a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
b = ['a', 'c', 'e']
c = check(a, b)

if c:
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
