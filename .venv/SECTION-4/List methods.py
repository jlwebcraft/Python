"""
List methods

append()     Adds an element at the end of the list
clear()      Removes all the elements from the list
copy()       Returns a copy of the list
count()      Returns the number of elements with the specified value
extend()     Add the elements of a list (or any iterable) to the end of the current list
index()      Returns the index of the first element with the specified value
insert()     Adds an element at the specified position
pop()        Removes the element at the specified position
remove()     Removes the first item with the specified value
reverse()    Reverses the order of the list
sort()       Sorts the list

"""

# 1. append()
list1 = [1, 2, 3]
list1.append(4)
print(list1)   # [1, 2, 3, 4]

# 2. clear()
list2 = [1, 2, 3]
list2.clear()
print(list2)   # []

# 3. copy()
list3 = [1, 2, 3]
list_copy = list3.copy()
print(list_copy)   # [1, 2, 3]

# 4. count()
list4 = [1, 2, 2, 3, 2]
print(list4.count(2))   # 3

# 5. extend()
list5 = [1, 2, 3]
list5.extend([4, 5])
print(list5)   # [1, 2, 3, 4, 5]

# 6. index()
list6 = ["a", "b", "c", "b"]
print(list6.index("b"))   # 1

# 7. insert()
list7 = [1, 3, 4]
list7.insert(1, 2)
print(list7)   # [1, 2, 3, 4]

# 8. pop()
list8 = [10, 20, 30,40]
print(list8.pop(1))   # 20
print(list8)          # [10, 30]
# If no index is given, removes the last item:
print(list8.pop()) #40

# 9. remove()
list9 = [1, 2, 3, 2]
list9.remove(2)
print(list9)   # [1, 3, 2]

# 10. reverse()
list10 = [1, 2, 3]
list10.reverse()
print(list10)   # [3, 2, 1]

# 11. sort()
list11 = [3, 1, 4, 2]
list11.sort()
print(list11)   # [1, 2, 3, 4]
