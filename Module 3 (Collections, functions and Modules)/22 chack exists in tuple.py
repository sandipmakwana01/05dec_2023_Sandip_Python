"""Write a Python program to check whether an element exists within a
tuple."""
a = (1,2,3,4,5)
b = 6
if b in a:
    print(f'{b} : Exists in a Tuple')
else:
    print(f'{b} : Dose not exists in a Tuple')
