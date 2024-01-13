"""Write a Python program to convert degree to radian"""
import math

def degrees(x):
    r = x * (math.pi / 180)
    return r

# Example usage:
a = float(input("Enter degree: "))
b = degrees(a)

print(f"degrees: {a} \nradians: {b}")
