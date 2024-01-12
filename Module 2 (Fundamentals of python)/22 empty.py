"""Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string"""

def flchar(x):
    if len(x) < 2:
        return "" 
    else:
        return x[:2] + x[-2:]

s1 = "python"
s2 = "a"
s3 = "abcdef"

r1 = flchar(s1)
r2 = flchar(s2)
r3 = flchar(s3)

print(f"Original: {s1}, Result: {r1}")
print(f"Original: {s2}, Result: {r2}")
print(f"Original: {s3}, Result: {r3}")
