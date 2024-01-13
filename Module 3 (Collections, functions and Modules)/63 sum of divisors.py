"""Write a Python program to returns sum of all divisors of a number"""
def divisors(x):
    n = 0
    for i in range(1, x + 1):
        if x % i == 0:
            n += i
    return n

a = int(input("Enter a number: "))
b = divisors(a)

print(f"The sum of divisors of {a} is: {b}")
