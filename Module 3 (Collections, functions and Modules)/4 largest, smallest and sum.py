"""Write a Python function to get the largest number, smallest num and sum
of all from a list"""
def lss(x):
    largest_num = max(x)
    smallest_num = min(x)
    sum_list = sum(x)

    print(f'Largest Number of :{largest_num}')
    print(f'Smallest Number of :{smallest_num}')
    print(f'Sum of list :{sum_list}')

a =[1,2,3,4,5,6,7,8,9,10]
lss(a)