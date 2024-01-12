"""Differentiate between append () and extend () methods?"""

a = [1,2,3,4,5]
a.append(5)
print(a)

b = [11,22,33,44,55]
c = [111,222,333,444,555]
b.extend(c)
print(b)