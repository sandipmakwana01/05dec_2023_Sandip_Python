"""Write a Python program to convert a list of tuples into a dictionary."""
def convert(n):
    result_dict = {}
    for key, value in n:
        result_dict[key] = value
    return result_dict

a = [(1, 'a'), (2, 'b'), (3, 'c')]

b = convert(a)

print(b)
