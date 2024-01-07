""" Write a Python program to get the Factorial number of given number. """

n = int(input("Enter a Number :"))
r=1
for i in range(n,0,-1):
    # result *= i
    r = r *i
    # result=1*5
    # result=1*5*4
    # result=1*5*4*3
    # result=1*5*4*3*2
    # result=1*5*4*3*2*1
print(r)

