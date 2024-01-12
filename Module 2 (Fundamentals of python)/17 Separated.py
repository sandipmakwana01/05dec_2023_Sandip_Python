"""Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string."""

def counts(a):
    a = a.lower()
    
    b = a.split()

    c = {}

    for x in b:
        x = x.strip(".,!?")

        c[x] = c.get(x, 0) + 1

    return c

y = "This is a simple example. Simple is as simple does."
z = counts(y)

for x, count in z.items():
    print(f"'{x}': {count} time")
