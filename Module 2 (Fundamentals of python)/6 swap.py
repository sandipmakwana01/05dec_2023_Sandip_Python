"""Write python program that swap two number with temp variable and
without temp variable."""

# With temp variable
a = 5
b = 10
temp = a
a = b
b = temp
print("with temp variable:", a, b)

# Without temp variable
a = 5
b = 10
a, b = b, a
print("without temp variable:", a, b)
