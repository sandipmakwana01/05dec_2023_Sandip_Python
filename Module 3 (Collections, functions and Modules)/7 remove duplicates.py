"""Write a Python program to remove duplicates from a list."""

list1 = [1, 2, 2, 3, 4, 4, 5]

def remove(x):
    new_list = []
    for n in x:
        if n not in new_list:
            new_list.append(n)
    return new_list

remove(list1)

print("Original List:", list1)
print("List after removing duplicates :", remove(list1))
