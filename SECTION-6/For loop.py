"""
Loops

1-2-3-4-5-6-7......
Iterating / Iteration

print("Python")
print("Python")
print("Python")
print("Python")
print("Python")
print("Python")
print("Python")

DRY - Don't Repeat Yourself

Two Types of Loops:
For Loop:
    - Goes through an element/value means it scans through it.
    - Only works with String and Arrays
    - The rounds of the for loop is directly related to the length of the value
"""
### SYNTAX
"""
for var in range(start, stop, step)
    code here
    
deafults:
1. start is 0
2. step is 1
"""



"""
string = "12345"
for character in string:
    print(character)

#print from 99 to 1
for i in range(99,0,-1):
    print(i)

# Given a string print how many 'a' are there
x=0
str="aeroplane"
for i in str:
    if(i=='a'):
        x+=1
print(x)
"""

# Given a string print how many vowels are there
"""
x=0
str="THIS IS A STRING"
for i in str.lower():
    if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u'):
        x+=1
print(x)
"""