"""
Create a phone directory with a external named phonebook.txt it'll have columns/variables
Name     Address     Phone Number

Our program should be able to Create a new record of name, it should be able to update the record, also, it should be able
to Read all the data, it should be able to delete.

new_record(name, address, number)
update(number) -> Ask user to input new name address and phone number
display_info()
delete(name, number)
main() -> Menus to select.

The program will continue until user selects exit
"""

def new_record(name, address, number):
    with open("phonebook.txt", "a") as file:
        file.write(f"{name}\t{address}\t{number}\n")


def update(number):
    new_name = input("Enter the new name: ")
    new_address = input("Enter the new address: ")
    new_number = input("Enter the new number: ")

    try:
        with open("phonebook.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("Phonebook is empty.")
            return

        header = lines[0]
        lines = lines[1:]
        updated_lines = header

        for i in lines:
            if number == i.split("\t")[-1].strip():
                updated_lines += f"{new_name}\t{new_address}\t{new_number}\n"
            else:
                updated_lines += i

        with open("phonebook.txt", "w") as file:
            file.write(updated_lines)

        print("Record updated successfully.")
    except FileNotFoundError:
        print("Phonebook does not exist yet.")

def delete(name, number):
    try:
        with open("phonebook.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("Phonebook is empty.")
            return

        updated_lines = []
        record_deleted = False

        for line in lines:
            parts = line.strip().split("\t")
            if len(parts) >= 3 and parts[0] == name and parts[-1] == number:
                record_deleted = True
            else:
                updated_lines.append(line)

        with open("phonebook.txt", "w") as file:
            file.writelines(updated_lines)

        if record_deleted:
            print("Record deleted successfully.")
        else:
            print("No matching record found to delete.")

    except FileNotFoundError:
        print("Phonebook does not exist yet.")

def display_info():
    try:
        with open("phonebook.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("Phonebook is empty.")
            else:
                print("\n--- Phonebook Entries ---")
                for line in lines:
                    print(line.strip())
                print("-------------------------\n")
    except FileNotFoundError:
        print("Phonebook does not exist yet. Please add a record first.")

b = True
while b:
    print("Press 1 to add new record")
    print("Press 2 to update existing record")
    print("Press 3 to display phonebook")
    print("Press 4 to delete a record")
    print("Press 5 to exit")
    choice = input("Enter your choice: ")

    if choice=="1":
        name = input("Enter name: ")
        address = input("Enter address: ")
        number = input("Enter number: ")
        new_record(name, address, number)
        print("Record added successfully.")

    elif choice=="2":
        toUpdate = input("Enter number to update: ")
        update(toUpdate)

    elif choice=="3":
        display_info()

    elif choice == "4":
        del_name = input("Enter the name to delete: ")
        del_number = input("Enter the number to delete: ")
        delete(del_name, del_number)

    elif choice == "5":
        print("Exiting...")
        b = False

    else:
        print("Invalid choice, please try again.")