"""Write a Python function that takes two lists and returns true if they have
at least one common member."""

def common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return bool(set1.intersection(set2))

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

common(a, b)

if common(a,b):
    print("lists at least one common member.")
else:
    print("lists do not have any common members.")
