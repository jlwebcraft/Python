"""
Sets
1. No Duplicates
"""

a = {1, 2, 3, 4, 4}
print(a) # {1, 2, 3, 4}

a.remove(4)
print(a) # {1, 2, 3}

a.add(4)
print(a) # {1, 2, 3, 4}

print(a.union({1,4,6,7,10})) # {1, 2, 3, 4, 6, 7, 10}