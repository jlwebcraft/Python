"""
1. Structural Programming
2. Functional Programming
3. Object-Oriented Programming

Terminologies

Objects - The variables that contains classes
Class - The main machine of the OOP

Class Variable - The variables that are just inside a class
Data Members - All the variables and identifiers / functions that are inside a class
Methods - The functions inside a class
        - Applied on a value
        - With Dot Notation
self

Intantiation -It's a process of create of (an Instance with a class) / (object)


Constructors - __constructor__ -Dunder-DoubleUnderscore
"""

class Car:
    ## Class Code
    company_name = "Lamborghini,"
    estd = "1868"

    def __init__(self,arg1):
        self.arg1=arg1
        print(arg1)

    def __str__(self):
        return "It's a Huracan car"

    def __doc__(self):
        return "Help for Huracan is currently not available, Sorry!"

    def create_car(self, engine, fuel, wheels, color):
        print("A new car has been created with the following information:")
        print("Engine:", engine)
        print("Fuel:", fuel)
        print("Wheels:", wheels)
        print("Color:", color)


huracan = Car("arg1") #refer to line 29
print(huracan.company_name,huracan.estd)
print(huracan.arg1)
huracan.create_car("1000cc","Petrol","Alloy","Red")
print(huracan) #refer to line 33
print(huracan.__doc__()) #refer to line 36