"""Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings"""

def list(lst):
    count = 0
    for string in lst:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

a = ["level", "python", "radar", "hello", "abba", "xyzzy" ,"abba"]

list(a)

print("Number of strings with the same first and last character:", list(a))
