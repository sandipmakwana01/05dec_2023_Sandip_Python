"""Write a Python program to test whether a passed letter is a vowel or
not."""
l = input("Enter a letter: ")

if l.lower() in 'aeiou':
    print("Vowel")
else:
    print("Not a vowel")
