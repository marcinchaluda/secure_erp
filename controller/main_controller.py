from view import terminal as view
from controller import crm_controller, sales_controller, hr_controller
from os import system
from time import sleep


def load_module(option):
    if option == 1:
        crm_controller.menu()
    elif option == 2:
        sales_controller.menu()
    elif option == 3:
        hr_controller.menu()
    elif option == 0:
        return 0
    else:
        raise KeyError()


def display_menu():
    options = ["Exit program",
               "Customer Relationship Management (CRM)",
               "Sales",
               "Human Resources"]
    view.print_menu("Main menu", options)


def display_logotype():
    loading_screen = ""
    with open("logotype.txt", "r") as f:
        logotype = f.read()
        for i in range(21):
            system("clear")
            print(logotype)
            print("Loading:", loading_screen)
            loading_screen += ("%" * 3)
            sleep(0.12)


def menu():
    display_logotype()
    system("clear")
    option = None
    while option != '0':
        display_menu()
        try:
            option = view.get_input("Select module")
            system("clear")
            load_module(int(option))
        except KeyError:
            view.print_error_message("There is no such option!")
        except ValueError:
            view.print_error_message("Please enter a number!")
    view.print_message("Good-bye!")
