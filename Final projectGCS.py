########################
#   GCS-182
#   Project
#   Abdulaziz Bukhari ID:S23108571 / Abdulwahab Ghounim ID:S22107684 / Abdullah Alamoudi ID:S22107892
########################

# Import necessary libraries
import os 
from pathlib import Path  
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

contact = {}
current_file_name = ''

# Function to display the menu of the program 
def display_menu():
    clear_screen()
    print(f"Currently opened file: {current_file_name}\n")
    print("Menu:")
    print(" 1. Add contact ")
    print(" 2. View contact ")
    print(" 3. Search contact ")
    print(" 4. Update contact ")
    print(" 5. Delete contact ")
    print(" 6. Save contact ")
    print(" 7. Exit ")

def display_contact():
    clear_screen()
    print("{:<20} {:<20} {:<30}".format("Name", "Contact Number", "Email"))
    for key in contact:
        name, phone, email = key, contact[key][0], contact[key][1]
        print("{:<20} {:<20} {:<30}".format(name, phone, email))
    input("Press Enter to continue...")

# Function to add a new contact 
def add_contact():
    clear_screen()
    while True:
        name = input("Enter the contact's name: ")
        if name.isalpha():
            break
        else:
            clear_screen()
            print(f"Invalid name {name}. Please enter an alphabetical name only.")

    while True:
        phone = input("Enter the contact's phone number: ")
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            clear_screen()
            print(f"Invalid phone number '{phone}'. Please enter 10 digits only.")
            print(f"Name: {name}\tEmail: {contact.get(name, ('N/A', 'N/A'))[1]}")

    while True:
        email = input("Enter the contact's email: ")
        if '@' in email and '.' in email and any(domain in email for domain in ('com', 'org', 'net', 'sa', 'me', 'ru', 'ca', 'edu.sa')):
            break
        else:
            clear_screen()
            print(f"Invalid email address '{email}'. Please enter a valid email address.")
            print(f"Name: {name}\tPhone: {phone}")

    contact[name] = (phone, email)
    print(f"{name}'s contact added successfully.")

    add_another = input("Do you want to add another contact? (yes/no): ").lower()
    if add_another != 'yes':
        return


# Function to view contacts   
def view_contact():
    clear_screen()
    if not contact:
        print("The contact list is empty.")
    else:
        display_contact()

# Function to search contact 
def search_contact():
    clear_screen()
    search_term = input("Enter the contact's name or email: ").lower()

    if not search_term.strip():
        print("Search term cannot be empty.")
        input("Press Enter to continue...")
        return
##########################################################################################
    matches = []
    for key, value in contact.items():
        if search_term in key.lower() or search_term in value[1].lower():
            matches.append((key, value[0], value[1]))

    if matches:
        print("Matching contacts:")
        for index, match in enumerate(matches, start=1):
            print(f"{index}. Name: {match[0]}\tPhone: {match[1]}\tEmail: {match[2]}")
    else:
        print(f"No matching contacts found for '{search_term}'")

    input("Press Enter to continue...")
############################################################################################

# Function to update the contact information 
def update_contact():
    clear_screen()
    update_contact = input("Enter the contact's name to update: ").lower()
    if update_contact in contact:
        while True:
            phone = input("Enter the new phone number: ")
            if phone.isdigit() and len(phone) == 10:
                break
            else:
                clear_screen()
                print(f"Invalid phone number '{phone}'. Please enter 10 digits only.")
                print(f"Name: {update_contact}\tEmail: {contact.get(update_contact, ('N/A', 'N/A'))[1]}")
        
        while True:
            email = input("Enter the new email: ")
            if '@' in email and '.' in email and any(domain in email for domain in ('com', 'org', 'net', 'sa', 'me', 'ru', 'ca', 'edu.sa')):
                break
            else:
                clear_screen()
                print(f"Invalid email address '{email}'. Please enter a valid email.")
                print(f"Name: {update_contact}\tPhone: {phone}")
        
        contact[update_contact] = (phone, email)
        print(f"{update_contact}'s contact information updated.")
    else:
        print(f"{update_contact} is not found in the contact list.")
    input("Press Enter to continue...")

# Function to delete contact information 
def delete_contact():
    clear_screen()
    del_contact = input("Enter the contact's name to be deleted: ").lower()
    if del_contact in contact:
        confirm = input(f"Do you want to delete {del_contact}'s contact? (yes/no): ")
        if confirm.lower() == "yes":
            contact.pop(del_contact)
            print(f"{del_contact}'s contact deleted.")
        else:
            print("Deletion canceled.")
    else:
        print(f"{del_contact} is not found in the contact list.")
    input("Press Enter to continue...")

# Function to save contact to the opened file 
def save_contact(file_name):
    clear_screen()
    try:
        with open(file_name, 'w') as file:
            for name, (phone, email) in contact.items():
                file.write(f"{name},{phone},{email}\n")
        print(f"Contacts saved to {file_name}")
    except:
        print("Error saving contacts.")
    input("Press Enter to continue...")

# Function to select a existing or creating a new file 
def select_contact_file():
    while True:
        clear_screen()
        print("Choose an option:")
        print("1. Open an existing file")
        print("2. Create a new file for contacts")

        choice = input("Enter your choice (1-2): ").strip()  # Strip leading and trailing spaces

        if choice == '1':
            global current_file_name
            custom_file_name = input("Enter the existing file name(file should be .txt): ").strip()  # Strip leading and trailing spaces
            if custom_file_name:
                if not custom_file_name.endswith('.txt'):
                    custom_file_name += '.txt'
                if Path(custom_file_name).exists():
                    current_file_name = custom_file_name
                    print(f"Currently opened file: {current_file_name}")
                    print(f"Program will use: {current_file_name}")
                    time.sleep(1)
                    return current_file_name
                else:
                    print(f"File {custom_file_name} not found. Please enter a valid file name.")
                    input("Press Enter to continue...")
            else:
                print("Invalid file name. Please enter a valid file name.")
                input("Press Enter to continue...")
        elif choice == '2':
            new_file_name = input("Enter the new file name: ").strip()  # Strip leading and trailing spaces
            if new_file_name:
                if not new_file_name.endswith('.txt'):
                    new_file_name += '.txt'
                return new_file_name
            else:
                print("Invalid file name. Please enter a valid file name.")
                input("Press Enter to continue...")
        else:
            print("Invalid choice. Please choose between number 1 or 2.")
            input("Press Enter to continue...")


# Main Function 
def main():
    global current_file_name
    while True:
        file_name = select_contact_file()
        if file_name is None:
            break

        current_file_name = file_name
        file_path = Path(file_name)

        if not file_path.exists() and not file_name.endswith('.txt'):
            file_name += '.txt'
            current_file_name = file_name
            try:
                with open(file_name, 'w'):
                    pass
                print(f"New file {file_name} created.")
            except Exception as e:
                print(f"Error creating the new file: {e}")
                input("Press Enter to continue...")
                continue

        try:
            with file_path.open('r') as file:
                for line in file:
                    name, phone, email = line.strip().split(',')
                    contact[name.lower()] = (phone, email)
            print(f"\nContacts loaded from {file_name}")
        except FileNotFoundError:
            print(f"File {file_name} not found. Creating a new file.")

        while True:
            display_menu()
            try:
                choice = input("Enter your choice (1-7): ").strip()
                if not choice:  # Check if the input is empty
                    clear_screen()
                    print("Invalid choice. Please enter a number between 1 and 7.")
                    input("Press Enter to continue...")
                    continue

                choice = int(choice)
                if 1 <= choice <= 7:
                    if choice == 1:
                        add_contact()
                    elif choice == 2:
                        view_contact()
                    elif choice == 3:
                        search_contact()
                    elif choice == 4:
                        update_contact()
                    elif choice == 5:
                        delete_contact()
                    elif choice == 6:
                        save_contact(file_name)
                    elif choice == 7:
                        return
                else:
                    clear_screen()
                    print("Invalid choice. Please enter a number between 1 and 7.")
                    input("Press Enter to continue...")
            except ValueError:
                clear_screen()
                print("Invalid input. Please enter a number.")
                input("Press Enter to continue...")
# Exectuing the main function 
main()
