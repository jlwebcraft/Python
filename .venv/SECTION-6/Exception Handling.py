"""
Exception Handling

try... except...
"""
### SYNTAX:
"""
try:
    # This
    # If that doesn't work
except Error as variable:
    # This
    
if multiple
except (KeyError, Type error) as e:
"""


"""
dictionary = {"Apple": "A red fruit", "Banana": "A Yellow Fruit", "Orange": "A round fruit"}
try:
    print(dictionary["grapes"])
# If that doesn't work
except KeyError as e:
    print("Oh! That's not registered in our dictionary")
"""

"""
num = 1234
string = "1234"
try:
    print(num + string)
except TypeError as e:
    print("Sorry! Integer and String cannot be added together. Please use data types conversion to change either of them")
"""




"""
Common Built-in Exception Types
Exception Type	            Raised When...
Exception	                Base class for all exceptions (catch-all).
ArithmeticError	            Base for numeric errors.
ZeroDivisionError	        Division/modulo by zero.
OverflowError	            Numeric calculation exceeds limit.
FloatingPointError          Floating-point operation fails.
ValueError	                Function gets argument of right type but invalid value.
TypeError	                Operation applied to wrong type.
IndexError	                Index out of range in a sequence.
KeyError	                Key not found in a dictionary.
NameError	                Variable not defined.
FileNotFoundError           File or directory not found.
IOError / OSError	        Input/output operation fails.
ImportError	                Import fails.
ModuleNotFoundError	        Module not found.
AttributeError	            Attribute reference fails.
StopIteration	            next() called on exhausted iterator.
RuntimeError	            Generic runtime error.
MemoryError	                Out of memory.
AssertionError	            assert statement fails.
"""