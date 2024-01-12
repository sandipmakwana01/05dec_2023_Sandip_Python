"""Write a Python program to count occurrences of a substring in a string"""
def counts(a, b):
    x = a.count(b)
    return x

s1 = "hello world, hello universe, hello galaxy"
s2 = "hello"

a = counts(s1, s2)
print(f"Word '{s2}' is {a} times in the given string.")
