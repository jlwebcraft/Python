"""
Recursion - only works with functions()
          - funtion will call itself in it
re-occur  - recur
"""

# Printing 1 to 10 using recursion
"""
def printing(c=1):
    if(c<11):
        print(c)
        c+=1
        printing(c)

printing()
"""

# Create a function for factorial
"""
def fact(x):
    if(x==1 or x==0):
        return 1
    else:
        return x*fact(x-1)
print(fact(5))
print(fact(6))
print(fact(7))
"""