"""
Tuple
Immutable - Can't be changed
"""

a = (1, 2, 3, 4, 4)
print(a.count(4)) # 2

print(a[2]) # 3

print(a.index(3)) # 2

print(a.__add__((7, ))) # (1, 2, 3, 4, 4, 7)
print(a) # (1, 2, 3, 4, 4)

print(a.__mul__(2)) # (1, 2, 3, 4, 4, 1, 2, 3, 4, 4)