"""

File Handling

Handling some files (external)

CRUD - Create Read Update Delete
.txt
.csv
.xlsx

1. Open A File
   a. Variable method
   b. With method

read -r
write -w
append -a

"""

# file = open("test.txt", "r")
# print(file.read())
# file.close()
print("original")

with open("test.txt", "r") as file:
    print(file.read())

print("")


with open("test.txt", "w") as file:
    file.write("hello\nhello")
print("read,overwritten")
with open("test.txt", "r") as file:
    print(file.read())


with open("test.txt", "a") as file:
    file.write("\nhello\nhello")

print("")

print("read appended")
with open("test.txt", "r") as file:
    print(file.read())

print("")

print("Creating") # if no file with that name while using write or append


with open("test_new.txt", "w") as file:
    file.write("hello\nhello")

print("")

print("Deleting")

import os
os.system("del test_new.txt")