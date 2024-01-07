"""Write a Python program to count the number of characters (character
frequency) in a string"""

user = input("Enter a string: ")

for i in user:
    a= user.count(i)
    print(f"Character is : '{i}' time: {a} ")