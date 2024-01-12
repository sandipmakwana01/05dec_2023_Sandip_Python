"""Write a Python script to sort (ascending and descending) a dictionary by
value"""
def sort(x, reverse=False):
    return dict(
        sorted(
        x.items(), 
        key=lambda item: item[1], 
        reverse=reverse)
        )

a = {'apple': 3, 'banana': 1, 'orange': 2, 'grape': 4}

ascending = sort(a)
print("Sorted in ascending order:", ascending)

descending = sort(a, reverse=True)
print("Sorted in descending order:", descending)
