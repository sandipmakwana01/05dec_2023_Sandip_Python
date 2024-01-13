"""Write a Python function to calculate the factorial of a number (a
nonnegative integer)"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

x = factorial(5)

print(f"factorial of 5  is: {x}")
