"""Write a Python function to insert a string in the middle of a string"""
def insert_string_in_middle(a, b):
    n = len(a) // 2
    p = a[:n] + b + a[n:]
    return p

x = "abcdefgh"
y = "XYZ"

o = insert_string_in_middle(x, y)

print(f"Original: {x} \nResult: {o}")
