"""Write a Python program to count the occurrences of each word in a
given sentence"""
def count(s):
    x = {}
    a = s.split()

    for word in a:
        word = word.strip(".,?!").lower()
        if word in x:
            x[word] += 1
        else:
            x[word] = 1
    return x

n = "Write a Python program to count the occurrences of each word in a given sentence"

m = count(n)
for word, count in m.items():
    print(f"Word '{word}' is {count} times in the sentence.")
