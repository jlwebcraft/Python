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
For Loop - Goes through an element/value means it scans through it.
    - Only works with String and Arrays
    - The rounds of the for loop is directly related to the length of the value
While Loop
    -works with boolean only
"""
### SYNTAX
"""
while bool:
    code here
"""

"""
#print from 99 to 1
i=99
while i>=1:
    print(i)
    i-=1
"""
"""
# Given a string print how many 'a' are there
x=0
temp=0
str="aeroplane"
while temp<len(str):
    if(str[temp]=='a'):
        x+=1
    temp+=1
print(x)
"""

# Given a string print how many vowels are there
"""
x = 0
temp=0
str = "THIS IS A STRING"
while temp<len(str):
    if (str[temp].lower() in "aeiou"):
        x += 1
    temp+=1
print(x)
"""