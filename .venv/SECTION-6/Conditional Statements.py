"""
Conditional Statements

Operators

3. Comparison
4. Logical

Control Flow
Control Structure

Boolean Values

if False:
    # Execute code when condition1 is correct
elif False:
    # Execute code when condition2 is correct
elif False:
    # Execute the code when condition3 is correct
else:
    # Execute if none of the conditions are correct
"""
"""
if condition1:
    print("Condition 1 is true")
elif condition2:
    print("Condition 2 is true")
elif condition3:
    print("Condition 3 is true")
else:
    print("None of the conditions are true")
"""

"""
Given an age, find whether a person qualifies for a driver's license.
 - He should be older than 16 years of age.
"""

age = 14
if age >= 16:
    print("He qualifies for the driver's license")
else:
    print("He doesn't qualify for a driver's license")


"""
Given 3 numbers, a, b and c, find the greatest between the three.
"""

a = 10
b = 12
c = 3

if a > b and a > c:
    print("A is the greatest")
elif b > a and b > c:
    print("B is the greatest")
else:
    print("C is the greatest")
