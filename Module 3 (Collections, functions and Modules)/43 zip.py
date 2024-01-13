"""Why Do You Use the Zip () Method in Python?"""

a = ['sandip', 'fenill', 'nikul']
b = [25, 30, 22]

combining = [
    (name, age) 
    for name, age in zip(a, b)
]

print(combining)
