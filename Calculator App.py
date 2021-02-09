menu_list = ["Add", "Subtract","Multiply","Divide","Quit"]


def add(num1, num2):
    total = num1 + num2
    return total


def subtract(num1, num2):
    total = num1 - num2
    return total


def multiply(num1, num2):
    total = num1 * num2
    return total


def divide(num1, num2):
    total = num1 / num2
    return total


def user_input():
    global num1
    global num2
    print("\n" * 98)
    num1 = float(input("Please enter a number :"))
    print("\n" * 98)
    num2 = float(input("Please enter another number :"))
    print("\n" * 98)
    return num1, num2

def populate_menu(option):
    print("\n")
    for index, option in enumerate(option, 1):
        print(f"{index} - {option}")
    print("\n")


def selection_menu(menuList):
    print("---------------------------------------------------------")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = str(input("Please type one of the numbers from above to continue:"))
    print("---------------------------------------------------------")
    return main_user_input


def selection_menu_incorrect(menuList):
    print("---------------------------------------------------------")
    print("Incorrect selection, please try again")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = str(input("Please type one of the numbers from above to continue:"))
    print("---------------------------------------------------------")
    return main_user_input

def main():
    while True:
        main_user_input = selection_menu(menu_list)

        if main_user_input == '1' or main_user_input == "add" or main_user_input == "Add":
            user_input()
            print(num1, "+", num2, "=", add(num1, num2))
            main()

        elif main_user_input == '2' or main_user_input == "subtract" or main_user_input == "Subtract":
            user_input()
            print(num1, "-", num2, "=", subtract(num1, num2))
            main()

        elif main_user_input == '3' or main_user_input == "multiply" or main_user_input == "Multiply":
            user_input()
            print(num1, "*", num2, "=", multiply(num1, num2))
            main()

        elif main_user_input == '4' or main_user_input == "divide" or main_user_input == "Divide":
            user_input()
            print(num1, "/", num2, "=", divide(num1, num2))
            main()

        elif main_user_input == "5" or main_user_input == "quit" or main_user_input == "Quit":
            break

        else:
            incorrect_main()
            
            
def incorrect_main():            
    while True:
        main_user_input = selection_menu_incorrect(menu_list)
        if main_user_input == '1' or main_user_input == "add" or main_user_input == "Add": 
            user_input()
            print(num1, "+", num2, "=", add(num1, num2))
            main()

        elif main_user_input == '2' or main_user_input == "subtract" or main_user_input == "Subtract":
            user_input()
            print(num1, "-", num2, "=", subtract(num1, num2))
            main()

        elif main_user_input == '3' or main_user_input == "multiply" or main_user_input == "Multiply":
            user_input()
            print(num1, "*", num2, "=", multiply(num1, num2))
            main()

        elif main_user_input == '4' or main_user_input == "divide" or main_user_input == "Divide":
            user_input()
            print(num1, "/", num2, "=", divide(num1, num2))
            main()

        elif main_user_input == "5" or main_user_input == "quit" or main_user_input == "Quit":
            break
        else:
            incorrect_main()
 
main()                   