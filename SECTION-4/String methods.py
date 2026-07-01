"""
String methods

capitalize()   Converts the first character to upper case
casefold()     Converts string into lower case
center()       Returns a centered string
count()        Returns the number of times a specified value occurs in a string
encode()       Returns an encoded version of the string
endswith()     Returns true if the string ends with the specified value
find()         Searches the string for a specified value and returns the position of where it was found
format()       Formats specified values in a string
index()        Searches the string for a specified value and returns the position of where it was found
isalnum()      Returns True if all characters in the string are alphanumeric
isalpha()      Returns True if all characters in the string are in the alphabet
isascii()      Returns True if all characters in the string are ASCII characters
isdecimal()    Returns True if all characters in the string are decimals
isdigit()      Returns True if all characters in the string are digits
islower()      Returns True if all characters in the string are lower case
isnumeric()    Returns True if all characters in the string are numeric
isspace()      Returns True if all characters in the string are whitespaces
istitle()      Returns True if the string follows the rules of a title
isupper()      Returns True if all characters in the string are upper case
join()         Converts the elements of an iterable into a string
lower()        Converts a string into lower case
startswith()   Returns true if the string starts with the specified value
title()        Converts the first character of each word to upper case
translate()    Returns a translated string
upper()        Converts a string into upper case

"""

# 1. capitalize()
string1="python"
print(string1.capitalize()) #python

# 2. casefold()
string2="PYTHON"
print(string1.casefold()) #python

# 3. center()
string3="PYTHON PROGRAMMING"
print(string3.center(20)) #number should be greater than number of letters

# 4. count()
string4="PYTHON PROGRAMMING"
print(string4.count('M')) #case sensitive

# 5. encode()
string5="PYTHON😎"
print(string5.encode()) #b'PYTHON\xf0\x9f\x98\x8e'

# 6. endswith()
string6="PYTHON"
print(string6.endswith("ON")) #returns boolean

# 7. find()
string7="PYTHON PROGRAMMING"
print(string7.find("P")) #only returns where it was first found

# 8. format()
string8="{} PROGRAMMING {}"
print(string8.format("PYTHON","IS EASY"))  #PYTHON PROGRAMMING IS GOOD

# 9. index()
string9="PYTHON"
print(string9.index('O'))

# 10. isalnum()
string10 = "Python123"
print(string10.isalnum())   # True → letters + numbers allowed

# 11. isalpha()
string11 = "Python"
print(string11.isalpha())   # True → only letters

# 12. isascii()
string12 = "Python123"
print(string12.isascii())   # True → all ASCII characters

# 13. isdecimal()
string13 = "1234"
print(string13.isdecimal())  # True → only decimal numbers

# 14. isdigit()
string14 = "1234"
print(string14.isdigit())    # True → all digits

# 15. islower()
string15 = "python"
print(string15.islower())    # True → all characters are lowercase

# 16. isnumerical
string16 = "²34"
print(string16.isnumeric())  # True → numeric (includes superscript, fractions, etc.)

# 17. isspace()
string17 = "   "
print(string17.isspace())    # True → only whitespace

# 18. istitle()
string18 = "Python Programming"
print(string18.istitle())    # True → every word capitalized

# 19. issuper()
string19 = "PYTHON"
print(string19.isupper())    # True → all uppercase

# 20. join()
string20 = ["P","Y","T","H","O","N"]
print("".join(string20))     # PYTHON

# 21. lower()
string21 = "PYTHON"
print(string21.lower())      # python

# 22. startswith()
string22 = "PYTHON PROGRAMMING"
print(string22.startswith("PY"))   # True

# 23. translate()
string23 = "python"
table = str.maketrans({"p": "P"})
print(string23.translate(table))   # Python

# 24. upper()
string24 = "python"
print(string24.upper())      # PYTHON