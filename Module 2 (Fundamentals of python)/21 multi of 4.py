""" Write a Python function to reverses a string if its length is a multiple of 4."""

def multiple(x):
    if len(x) % 4 == 0:
        return x[::-1] 
    else:
        return x

s1 = "abcd"
s2 = "python"
s3 = "1234"

r1 = multiple(s1)
r2 = multiple(s2)
r3 = multiple(s3)

print(f"Original: {s1}, Result: {r1}")
print(f"Original: {s2}, Result: {r2}")
print(f"Original: {s3}, Result: {r3}")
