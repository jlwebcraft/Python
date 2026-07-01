"""
Dictionary Methods

CREATE
READ
UPDATE
DELETE

"""


### CREATE

# Create Table
db = {"Name": "Henry", "Age": 40, "Country": "US", "Income": 100000}


### READ

# Read Table / Dictionary
print(db)

# Read Variables / Columns / Keys
print(db.keys())
for i in db.keys():
    print(i)

# Read Records / Rows / Values
print(db.values())
for i in db.values():
    print(i)


### Update

# Update Variables / Columns / Keys
# delete exisiting then adding new one
db["Country code"]="US"

# Update Records / Rows / Values
db["Country"] = "Canada"
print(db)


### DELETE

# Delete Columns / Variables / Keys
del db["Country"]
print(db)

db.pop("Age")
print(db)