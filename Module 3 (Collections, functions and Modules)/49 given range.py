"""Write a Python function to check whether a number is in a given range"""
def rangee(x, y, z):
    return y <= x <= z

a = 25
min_num = 10
max_num = 30

if rangee(a, min_num, max_num):
    print(f"{a} is in the range between {min_num} and {max_num}.")
else:
    print(f"{a} is not in the range between {min_num} and {max_num}.")
