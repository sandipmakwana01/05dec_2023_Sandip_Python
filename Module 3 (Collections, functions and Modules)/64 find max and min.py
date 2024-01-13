"""Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers"""

a = [
    float(x) 
    for x in input("Enter decimal numbers separated by spaces: ").split()
    ]

max_num = max(a)
min_num = min(a)

if max_num is not None and min_num is not None:
    print(f"The maximum number is: {max_num}")
    print(f"The minimum number is: {min_num}")
else:
    print("The list is empty.")
