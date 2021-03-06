from model.crm import crm
from view import terminal as view
from os import system


def list_customers():
    list_of_customers = crm.read_content_from_file_in_nested_list()
    view.print_table(list_of_customers)


def add_customer():
    entry = view.get_inputs(['name', 'email', 'if subscribed(Yes-1, No-0)'])
    crm.append_nested_list_and_write_content(entry)


def update_customer():
    number = input("Please input number of customer: ")
    try:
        is_customer_index_valid(number)
        entry = view.get_inputs(['name', 'email', 'if subscribed(Yes-1, No-0)'])
        crm.update_nested_list_and_write_content(number, entry)
    except IndexError:
        view.print_error_message('There is no position with this number!')


def delete_customer():
    number = input("Please input number of customer: ")
    try:
        is_customer_index_valid(number)
        crm.delete_nested_list_and_write_content(number)
    except IndexError:
        view.print_error_message('There is no position with this number!')


def is_customer_index_valid(number):
    if int(number) == 0 or int(number) > len(crm.read_content_from_file_in_nested_list()):
        raise IndexError


def get_subscribed_emails():
    list_of_customers = crm.read_content_from_file_in_nested_list()
    list_of_subscribed_emails = []
    for customer in list_of_customers:
        if customer[3] == '1':
            list_of_subscribed_emails.append(customer[2])
    view.print_general_results(list_of_subscribed_emails, 'Subscribed emails')


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            system("clear")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
