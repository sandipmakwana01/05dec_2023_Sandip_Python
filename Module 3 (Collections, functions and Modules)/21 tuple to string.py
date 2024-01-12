"""Write a Python program to convert a tuple to a string."""
a = (1,2,3,4,5)
b = ''.join(map(str,a))

print("Tuple :", a)
print("Tuple in to String:", b)

