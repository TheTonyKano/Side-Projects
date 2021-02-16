import json
import pathlib
from datetime import date

#   Prompts
mainMenuList = ["Add Contact", "Update Contact", "Delete Contact", "Exit Application"]

def populate_menu(option):
    print("\n")
    for index, option in enumerate(option, 1):
        print(f"{index} - {option}")
    print("\n")


def selection_menu(menuList):
    print("\n" * 100)
    global main_user_input
    print("---------------------------------------------------------")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = input("Please type one of the numbers from above to continue:")
    print("---------------------------------------------------------")
    return main_user_input


def selection_menu_incorrect(menuList):
    print("\n" * 100)
    global main_user_input
    print("---------------------------------------------------------")
    print("Incorrect selection, please try again")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = input("Please type one of the numbers from above to continue:")
    print("---------------------------------------------------------")
    return main_user_input


def main_menu(): # Main Menu and Selection Menu
    print("\n" * 100)
    while True:
        selection_menu(mainMenuList)
        if main_user_input == "1":
            createContact()
        elif main_user_input == "2":
            updateContact()
        elif main_user_input == "3":
            deleteContact()
        elif main_user_input == "4":
            exit_application()
        else:
            while True:
                if main_user_input == "1":
                    createContact()
                elif main_user_input == "2":
                    updateContact()
                elif main_user_input == "3":
                    deleteContact()
                elif main_user_input == "4":
                    exit_application()
                else:
                    selection_menu_incorrect(mainMenuList)

#   Account Management
def createContact():
    field = input("Please enter the job field the contact works in: ")
    company = input("Please enter the company the contact works in: ")
    firstname = input("Please enter the first name of the contact: ")
    lastname = input("Please enter the last name of the contact: ")
    phoneNumber = input("Please enter the contact's phone number: ")
    emailaddress = input("Please enter the email address of the contact: ")
    create_account(field, company, phoneNumber, firstname, lastname, emailaddress)

def create_account(field, company, phoneNumber, firstname, lastname, emailaddress):
    field_to_db(field)
    company_to_db(field, company)
    firstname_to_db(field, firstname, company)
    lastname_to_db(field, lastname, company)
    phoneNumber_to_db(field, phoneNumber, company)
    email_to_db(field, emailaddress, company)
    return print("Account has been created!")


def field_to_db(field): 
    directory[field] = {}
    output_db_to_file(directory)

def company_to_db(field, company_output): 
    directory[field][company_output] = {}
    output_db_to_file(directory)
    
def firstname_to_db(field, firstname_input, company_input): 
    directory[field][company_input]['FirstName'] = firstname_input
    output_db_to_file(directory)

def lastname_to_db(field, lastname_output, company_input):
    directory[field][company_input]['LastName'] = lastname_output
    output_db_to_file(directory)

def phoneNumber_to_db(field, phoneNumber_output, company_input): 
    directory[field][company_input]['Phone'] = phoneNumber_output
    output_db_to_file(directory)

def email_to_db(field, email_address_output, company_input): 
    directory[field][company_input]['Email_Address'] = email_address_output
    todays_date = date.today()
    directory[field][company_input]['Last Contacted Date'] = str(todays_date)
    output_db_to_file(directory)



#   Database Management
def output_db_to_file(directory): # Write Dictionary Memory to file
    with open('directory.json', 'w') as temp_dict:
        json.dump(directory, temp_dict)
        return directory 


def check_db_file(): # Retrieve Dictionary from JSON to Memory
    file_path = pathlib.Path("directory.json")
    while True:
        if file_path.exists():
            break
        else:
            blank_dict = {} #Makes new DB if one does not exist
            with open('directory.json', 'w') as create_file:
                json.dump(blank_dict, create_file)
        load_userdb()
        break


def load_userdb():
    check_db_file()
    with open('directory.json', 'r') as temp_dict:
        directory = json.load(temp_dict)
        return directory
    
    
#   Load Directory prior to Start of program
directory = load_userdb()

#   Start program
main_menu()
