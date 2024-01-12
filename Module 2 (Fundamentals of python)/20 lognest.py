"""Write a Python function that takes a list of a and returns the length of the longest one"""
def longest(x):
    if not x:
        return 0  

    m = len(x[0]) 

    for l in x[1:]:
        n = len(l)
        if n > m:
            m = n
    return m

a = ["apple", "banana", "orange", "strawberry", "kiwi"]
print("Length of the longest l:", longest(a))
