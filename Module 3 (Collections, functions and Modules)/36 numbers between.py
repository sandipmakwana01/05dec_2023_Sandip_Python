"""Write a Python script to print a dictionary where the keys are numbers
between 1 and 15"""

my_dict = {
    key: f"value_{key}" 
    for key in range(1, 16)
    }

print(my_dict)
