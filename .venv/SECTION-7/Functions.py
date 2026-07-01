"""
Functions

1. Structural Programming
2. Functional Programming - Functions
3. Object-Oriented Programming (OOP)

Functional Programming means the programming done using functions.

Function as a machine that takes in inputs and gives out output.
- Action - Predetermined - Code that goes in the function
- Input - Arguments while calling the function
- Output - Result

IPO = Input Processing Output

f(x) = mx + c

Two Parts of Function
1. Definition
2. Calling

##naming

Snake Method - function_name     hello_world

CamelCapitalization - FunctionName     HelloWorld

functionName     helloWorld

functionname     helloworld
"""

"""------------------------------------------------------------------
def print_hello():
    print("Hello_world")

print_hello()
print_hello()
print_hello()
print_hello()

Arguments -assumed -while defining the function
Parameters -given by user -while calling the function
Arguments and Parameters should be equal

None - default function return value--------------------------------return0
"""

# Create a python function for f(x) = mx + c--------------------last
"""
def f(x):
    m=1
    c=1
    print(m*x + c)

f(2)
f(3)
"""


# addition function
"""
def add(first, second):
    print(first + second)

add(1,7)
add(1,5)
"""


# setting output/return value---------------------------return1
"""
def hello(name):
    return "hello " +name

print(hello("John"))
"""

# Write a python funtion to validate age of a user for driver's license. age should be taken as an argument
"""
def license(age):
    if(age>=16):
        print("valid age")
    else:
        print("not a valid age")

license(22)
license(14)
license(17)
"""

# write a python program to print x to 1 using for loop. x should be taken using argument
"""
def loop(x):
    for i in range(x,0,-1):
        print(i)
loop(7)
loop(23)
"""